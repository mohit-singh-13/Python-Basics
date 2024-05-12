# import pymongo
from pymongo import MongoClient
from bson import ObjectId

# client = pymongo.MongoClient("mongodb+srv://mohit:BelieveSingh1@cluster0.izxqtso.mongodb.net/")
client = MongoClient("mongodb+srv://mohit:<password>@cluster0.izxqtso.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]

# print("Client: ", client)
# print("DB: ", db)
print("Video: ", video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}. Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name":name, "time":time})

def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': {"name": name, "time": time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice : ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video title: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()