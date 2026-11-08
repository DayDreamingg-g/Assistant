import subprocess
import win32gui
import win32con
import pywintypes
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QToolButton, QLabel
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
import sys

discord_exe_path = "C:/Users/facei/AppData/Local/Discord/Discord.exe"
discord_app_name = " - Discord"
spotify_exe_path = "C:/Users/facei/AppData/Roaming/Spotify/Spotify.exe"
spotify_app_name = "Spotify"
steam_exe_path = "C:/Program Files (x86)/Steam/steam.exe"
steam_app_name = "Steam"
browser_exe_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
browser_app_name = "Chrome"

def main():
    visual_box()

def visual_box():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("DayDreamingg-g Assistant")
    window.resize(900, 600)
    window.setStyleSheet("background-color: #151515;")
    layout = QHBoxLayout()
    layout.setSpacing(12)
    layout.setContentsMargins(25, 25, 25, 25)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window.setLayout(layout)

    discord_tile = create_app_tile("Discord", "icons/discord.ico")
    discord_tile.setFixedSize(150, 180)

    button_discord = QToolButton()
    button_discord.setText("Discord")
    button_discord.setIcon(QIcon("icons/discord.ico"))
    button_discord.setIconSize(QSize(48, 48))
    button_discord.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
    button_spotify = QPushButton("Spotify")
    button_steam = QPushButton("Steam")
    button_browser = QPushButton("Browser")
    button_exit = QPushButton("Exit the program")
    layout.addWidget(discord_tile)
    layout.addWidget(button_discord)

    layout.addWidget(button_spotify)
    layout.addWidget(button_steam)
    layout.addWidget(button_browser)
    layout.addWidget(button_exit)
    button_discord.clicked.connect(lambda: launch_app(discord_app_name, discord_exe_path))
    button_discord.setFixedSize(100, 90)
    button_spotify.clicked.connect(lambda: launch_app(spotify_app_name, spotify_exe_path))
    button_spotify.setFixedSize(100, 45)
    button_steam.clicked.connect(lambda: launch_app(steam_app_name, steam_exe_path))
    button_steam.setFixedSize(100, 45)
    button_browser.clicked.connect(lambda: launch_app(browser_app_name, browser_exe_path))
    button_browser.setFixedSize(100, 45)
    button_exit.clicked.connect(window.close)
    button_exit.setFixedSize(100, 45)
    #layout.addStretch()
    window.show()
    app.exec()

def create_app_tile(app_name, icon_path):
    #pass
    tile = QWidget()
    tile_layout = QVBoxLayout()
    tile.setLayout(tile_layout)

    tile_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    icon_label = QLabel()
    icon_label.setPixmap(QIcon(icon_path).pixmap(48,48))

    icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    tile_layout.addWidget(icon_label)

    text_label = QLabel()
    text_label.setText(app_name)
    text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    tile_layout.addWidget(text_label)

    return tile

def launch_app(app_name, exe_path):
    search_data = [app_name, False]
    win32gui.EnumWindows(check_window, search_data)

    if search_data[1] == False:
        try:
            subprocess.Popen([exe_path])

        except OSError as e:
            print(e)


def check_window(hwnd, search_data):
    title = win32gui.GetWindowText(hwnd)

    if search_data[0] in title and "Overlay" not in title:
        print(title)
        if win32gui.IsWindowVisible(hwnd) == True:
            search_data[1] = True
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

            try:
                win32gui.SetForegroundWindow(hwnd)
            except pywintypes.error:
                print("Failed to focus window")


if __name__ == "__main__":
    main()
