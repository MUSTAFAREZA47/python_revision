from pymongo import MongoClient
from bson.objectid import ObjectId  # Import ObjectId to handle MongoDB IDs properly

# MongoDB Connection
try:
    # MONGODB_URI=mongodb+srv://mustafareza47:ahmed123@cluster0.lfmuq.mongodb.net
    client = MongoClient('mongodb+srv://ahmed_python:LkAep0UhD2IXSGzF@cluster0.lfmuq.mongodb.net/', tls=True, tlsAllowInvalidCertificates=True)
    db = client['youtube_video_manager']
    video_collections = db['videos']
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Error connecting to MongoDB:", e)
    exit(1)  # Exit the program if connection fails

# Function to list all YouTube videos
def list_all_youtube_videos():
    print("\n" + "#" * 30 + "\n")
    for video in video_collections.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['duration']}")
    print("\n" + "#" * 30 + "\n")

# Function to add a YouTube video
def add_youtube_video(name, video_duration):
    try:
        result = video_collections.insert_one({"name": name, "duration": video_duration})
        print(f"Video added successfully! Video ID: {result.inserted_id}")
    except Exception as e:
        print("Error adding video:", e)

# Function to update a YouTube video
def update_youtube_video(video_id, name, video_duration):
    try:
        result = video_collections.update_one(
            {"_id": ObjectId(video_id)}, 
            {"$set": {"name": name, "duration": video_duration}}
        )
        if result.matched_count:
            print("Video updated successfully!")
        else:
            print("No video found with the given ID.")
    except Exception as e:
        print("Error updating video:", e)

# Function to delete a YouTube video
def delete_youtube_video(video_id):
    try:
        result = video_collections.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("Video deleted successfully!")
        else:
            print("No video found with the given ID.")
    except Exception as e:
        print("Error deleting video:", e)

# Main function
def main():
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_youtube_videos()
            case "2":
                name = input("Enter the name of the video: ")
                video_duration = input("Enter the duration of the video: ")
                add_youtube_video(name, video_duration)
            case "3":
                video_id = input("Enter the ID of the video to update: ")
                name = input("Enter the new name of the video: ")
                video_duration = input("Enter the new duration of the video: ")
                update_youtube_video(video_id, name, video_duration)
            case "4":
                video_id = input("Enter the ID of the video to delete: ")
                delete_youtube_video(video_id)
            case "5":
                print("Exiting the app. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

# Run the main function
if __name__ == '__main__':
    main()
