import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Chanvi")
    while True:
        x = input("Enter what you want me to speak:")
        if x == "quit":
            os.system("say 'Bye.Have a good day.'")
            break
        command = f"say {x}"
        os.system(command)
