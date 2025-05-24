import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")


# Step 1: Get user input for the desired Billboard date
date = input("Enter a date (YYYY-MM-DD): ")

# Step 2: Build the Billboard URL with headers to mimic a browser
url = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises HTTPError if not 200
except requests.exceptions.RequestException as e:
    print(f"❌ Failed to fetch Billboard data: {e}")
    sys.exit(1)

# Step 3: Parse the Billboard page and extract song titles
soup = BeautifulSoup(response.text, 'html.parser')

# Billboard structure: each song title is inside <li><ul><li><h3>...</h3>
songs = [song.getText().strip() for song in soup.select("li ul li h3")]

if not songs:
    print("❌ No songs found on the Billboard page. The structure may have changed.")
    sys.exit(1)

print(f"✅ Found {len(songs)} songs from Billboard Hot 100 on {date}")

# Step 4: Authenticate with Spotify
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id= os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret= os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri= os.getenv("SPOTIPY_REDIRECT_URI"),
        scope='playlist-modify-private'
    ))
    user_id = sp.current_user()['id']
except Exception as e:
    print(f"❌ Spotify authentication failed: {e}")
    sys.exit(1)

# Step 5: Search each song on Spotify and collect URIs
song_uris = []
year = date.split("-")[0]

print("🔍 Searching for songs on Spotify...")
for song in songs:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except (IndexError, KeyError):
        print(f"⚠️  '{song}' not found on Spotify.")

print(f"✅ {len(song_uris)} songs matched on Spotify")

# Step 6: Create a new playlist on Spotify
try:
    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"Billboard Hot 100 - {date}",
        public=False,
        description=f"Top 100 songs from Billboard on {date}"
    )
    sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
    print(f"🎉 Playlist created: 'Billboard Hot 100 - {date}' with {len(song_uris)} songs")
except Exception as e:
    print(f"❌ Failed to create playlist or add songs: {e}")
