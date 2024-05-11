import sqlite3

connection = sqlite3.connect('youtube_videos.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 70)
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]}, Duration: {row[2]}")
    print("\n")
    print("*" * 70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    connection.commit()

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    connection.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    connection.commit()

def main():
    while True:
        print("\nYouTube Manager")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video details")
        print("4. Delete a YouTube Video")
        print("5. Exit the app")
        
        choice = input("Enter your choice : ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    connection.close()

if __name__ == "__main__":
    main()