import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file) #<- load/read from the file and convert string to json format
            # print(type(test)) #type is a list but behind the scenes is a JSON list
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):     #<-We need to create a helper method to save data to a file. Whenever data needs to be written or updated, this method should be called with the data, and it will handle saving it.
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}, name: {video['name']} duration: {video['time']}")
    print("*"*50)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be update : "))
    if 1 <= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted : "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def main():
    videos = load_data()   #<- we will design a method where we load the data from a file i.e. youtube.txt instead of storing a value in array 
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        
        match choice :
            case '1' :
                list_all_videos(videos)
            case '2' :
                add_video(videos)
            case '3' :
                update_videos(videos)
            case '4' :
                delete_videos(videos)
            case '5' :
                break
            case _:
                print("Invalid Choice")  
                
if __name__ == "__main__":
    main()    
            











#Art of start a project
#>start with while loop so that terminal will ask questions to the users continiously until they opted to exit
# while True:
#     print("\n Youtube Manager | choose an option ")
#     print("1. List all youtube videos ")
#     print("2. Add a youtube video ")
#     print("3. Update a youtube video details ")
#     print("4. Delete a youtube video ")
#     print("5. Exit the app ")
#     choice = input("Enter your choice")
#> making match with the function call in the case one by one according to the input given by users from 1 to 5 case
#    match choice :
#         case '1' :
#             list_all_videos(videos)
#         case '2' :
#             add_video(videos)
#         case '3' :
#             update_videos(videos)
#         case '4' :
#             delete_videos(videos)
#         case '5' :
#             break
#         case _:
#             print("Invalid Choice") 
#> then make a entry point where code starts executing i.e. main()