import subprocess
import win32gui
import win32con
import pywintypes
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QMouseEvent
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
    window.setObjectName("main_window")
    window.setStyleSheet("#main_window { background-color: #151515; }")
    layout = QHBoxLayout()
    layout.setSpacing(12)
    layout.setContentsMargins(25, 25, 25, 25)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window.setLayout(layout)

    discord_tile = create_app_tile("Discord", "icons/discord.ico")
    discord_tile.clicked.connect(lambda: launch_app(discord_app_name, discord_exe_path))

    spotify_tile = create_app_tile("Spotify", "icons/spotify.png")
    spotify_tile.clicked.connect(lambda: launch_app(spotify_app_name, spotify_exe_path))

    steam_tile = create_app_tile(app_name="Steam", icon_path="icons/steam.png")
    steam_tile.clicked.connect(lambda: launch_app(steam_app_name, steam_exe_path))

    browser_tile = create_app_tile(app_name="Browser", icon_path="icons/browser.png")
    browser_tile.clicked.connect(lambda: launch_app(browser_app_name, browser_exe_path))



    button_exit = QPushButton("Exit the program")
    layout.addWidget(discord_tile)
    layout.addWidget(spotify_tile)
    layout.addWidget(steam_tile)
    layout.addWidget(browser_tile)


    layout.addWidget(button_exit)

    button_exit.clicked.connect(window.close)
    button_exit.setFixedSize(110, 45)

    window.show()
    app.exec()

class AppTile(QWidget):

    clicked = pyqtSignal()

    def enterEvent(self, event):
        self.setStyleSheet("AppTile {background-color: #3A3A3A; border-radius: 12px;}; QLabel {background-color: transparent;};")

    def leaveEvent(self, event):
        self.setStyleSheet("AppTile {background-color: #292929; border-radius: 12px;}; QLabel {background-color: transparent;};")

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event is not None and event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

    def set_tile_color(self, event):
        pass


def create_app_tile(app_name, icon_path):

    tile = AppTile()
    tile.setFixedSize(150, 180)
    tile.setAttribute(Qt.WidgetAttribute.WA_StyledBackground,True)
    tile.setStyleSheet("AppTile { background-color: #292929; border-radius: 12px; } QLabel { background-color: transparent; }")
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
        if  win32gui.IsWindowVisible(hwnd):
            search_data[1] = True
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

            try:
                win32gui.SetForegroundWindow(hwnd)
            except pywintypes.error:
                print("Failed to focus window")


if __name__ == "__main__":
    main()
