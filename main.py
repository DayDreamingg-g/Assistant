import subprocess
import win32gui
import win32con
import pywintypes
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QLabel, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QMouseEvent
import sys
from functools import partial

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

    apps = {
        "Discord": ("icons/discord.ico", " - Discord", "C:/Users/facei/AppData/Local/Discord/Discord.exe"),
        "Spotify": ("icons/spotify.png", "Spotify", "C:/Users/facei/AppData/Roaming/Spotify/Spotify.exe"),
        "Steam": ("icons/steam.png", "Steam", "C:/Program Files (x86)/Steam/steam.exe"),
        "Browser": ("icons/browser.png", "Chrome", "C:/Program Files/Google/Chrome/Application/chrome.exe")
    }

    for name in apps:
        icon_path, app_name, exe_path = apps[name]

        tile = create_app_tile(name, icon_path)
        layout.addWidget(tile)

        tile.clicked.connect(partial(launch_app, app_name, exe_path))

    button_exit = QPushButton("Exit the program")

    layout.addWidget(button_exit)

    button_exit.clicked.connect(window.close)
    button_exit.setFixedSize(110, 45)

    window.show()
    app.exec()

class AppTile(QWidget):

    clicked = pyqtSignal()

    def enterEvent(self, event):
        self.set_tile_color(color="#3A3A3A")

    def leaveEvent(self, event):
        self.set_tile_color(color="#292929")

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event is not None and event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

    def set_tile_color(self, color):
        self.setStyleSheet(f"AppTile {{background-color: {color}; border-radius: 12px;}}; QLabel {{ background-color: transparent; }}")

def create_app_tile(app_name, icon_path):

    tile = AppTile()
    tile.setFixedSize(150, 180)
    tile.setAttribute(Qt.WidgetAttribute.WA_StyledBackground,True)
    tile.set_tile_color(color="#292929")
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
    search_data = {
        "app_name": app_name,
        "hwnd": None
    }

    win32gui.EnumWindows(check_window, search_data)

    if search_data["hwnd"] is not None:
        focus_window(search_data["hwnd"])
        return

    try:
        subprocess.Popen([exe_path])
    except OSError as e:
        QMessageBox.critical(None, "Launch Error", str(e))

def check_window(hwnd, search_data):
    title = win32gui.GetWindowText(hwnd)

    if search_data["app_name"] in title and "Overlay" not in title and win32gui.IsWindowVisible(hwnd):
        search_data["hwnd"] = hwnd

    return True

def focus_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    try:
        win32gui.SetForegroundWindow(hwnd)
    except pywintypes.error:
        print("Failed to focus window")

if __name__ == "__main__":
    main()
