import subprocess
import win32gui
import win32con
import pywintypes

def main():
    jarvis()
    # win32gui.EnumWindows(check_window, None)

def check_window(hwnd, search_data):
    title = win32gui.GetWindowText(hwnd)

    if search_data[0] in title and "Overlay" not in title:
        print(title)
        if win32gui.IsWindowVisible(hwnd) == True:
            # print("Window is visible")
            search_data[1] = True
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            # win32gui.SetForegroundWindow(hwnd)

            try:
                win32gui.SetForegroundWindow(hwnd)
            except pywintypes.error:
                print("Failed to focus window")


        # else:
            # print("Window is hiden try to start up")
        # subprocess.Popen(["C:/Users/facei/AppData/Local/Discord/Discord.exe"])

        # print(win32gui.IsIconic(hwnd))


        # search_data[1] = True

def jarvis():
    print("Hello, I'm DayDreamingg-g assistant.")
    while True:
        print("What you want to start up? \n Write in console number of program would you like to launch. \n 1. Discord \n 2. Spotify \n 3. Steam \n 4. Browser \n 5. Stop Assistant.")

        choice = input("So, what do you want: ")

        if choice == "1":
            print("Try to find Discord.exe")
            app_name = " - Discord"
            exe_path = "C:/Users/facei/AppData/Local/Discord/Discord.exe"

        elif choice == "2":
            print("Try to find Spotify.exe")
            app_name = "Spotify"
            exe_path = "C:/Users/facei/AppData/Roaming/Spotify/Spotify.exe"

        elif choice == "3":
            print("Try to Steam.exe")
            app_name = "Steam"
            exe_path = "C:/Program Files (x86)/Steam/steam.exe"
        elif choice == "4":
            print("Try to GoogleChrome.exe")
            app_name = "Chrome"
            exe_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        elif choice == "5":
            print("Stop the program.")
            break

        else:
            print("Invalid choice")
            continue

        search_data = [app_name, False]
        win32gui.EnumWindows(check_window, search_data)

        if search_data[1] == False:
            # print("Window found")

            try:
                # print("Try to start up app")
                subprocess.Popen([exe_path])

            except OSError as e:
                print(e)
if __name__ == "__main__":
    main()

# subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])