import json


def load_youtube_videos():
    try:
        with open("youtube_videos.txt", "r") as file:
            return json.load(file)
            print("ahmed")
    except FileNotFoundError:
        return []
    finally:
        print("Loading youtube videos")


def save_youtube_helper(videos):
    with open("youtube_videos.txt", "w") as file:
        json.dump(videos, file)


def list_all_youtube_videos(videos):
    print("\n")
    print("#" * 30)
    print("\n")

    for index, video in enumerate(videos):
        print(f"{index + 1}. {video['title']}, Duration - {video['time']}")
    
    print("\n")
    print("#" * 30)
    print("\n")


def add_youtube_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"title": name, "time": time})
    save_youtube_helper(videos)
    print("Video added successfully")


def update_youtube_video(videos):
    list_all_youtube_videos(videos)
    index = int(input("Enter the index of the video to update: ")) - 1
    if index < 0 or index >= len(videos):
        print("Invalid index")
        return exit()
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos[index] = {"title": name, "time": time}
    save_youtube_helper(videos)
    print("Video updated successfully")

    
def delete_youtube_video(videos):
    list_all_youtube_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if index < 0 or index >= len(videos):
        print("Invalid index")
        return exit()
    del videos[index]
    save_youtube_helper(videos)
    print("Video deleted successfully")


def main():
    videos = load_youtube_videos()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_youtube_videos(videos)
                # print("Listing all youtube videos")
            case "2":
                add_youtube_video(videos)
                # print("Adding a youtube video")
            case "3":
                update_youtube_video(videos)
                # print("Updating a youtube video")
            case "4":
                delete_youtube_video(videos)
                # print("Deleting a youtube video")
            case "5":
                print("Exiting the app")
                break
            case _:
                print("Invalid choice. Please try again")



if __name__ == "__main__":
    main()
