import subprocess
import pywin32

def main():
    print("Hello, I'm DayDreamingg-g assistant.")
    while True:
        print("What you want to start up? \n Write in console number of program would you like to launch. \n 1. Discord \n 2. Spotify \n 3. Steam \n 4. Browser \n 5. Stop Assistant.")

        choice = input("So, what do you want: ")

        if choice == "1":
            print("Try to Discord.exe")
            try:
                subprocess.Popen(["C:/Users/facei/AppData/Local/Discord/Discord.exe"])
            except:
                print("Failed to start up Discord.exe")
        elif choice == "2":
            print("Try to Spotify.exe")
            try:
                subprocess.Popen(["C:/Users/facei/AppData/Roaming/Spotify/Spotify.exe"])
            except:
                print("Failed to start up Spotify.exe")
        elif choice == "3":
            print("Try to Steam.exe")
            try:
                subprocess.Popen(['C:/ProgramFiles(x86)/Steam/steam.exe'])
            except:
                print("Failed to start up Steam.exe")
        elif choice == "4":
            print("Try to GoogleChrome.exe")
            try:
                subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])
            except:
                print("Failed to start up your browser.")
        elif choice == "5":
            print("Stop the program.")
            break

if __name__ == "__main__":
    main()
