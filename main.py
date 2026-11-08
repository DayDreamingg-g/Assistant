import sys
import subprocess
from functools import partial

from window_manager import find_window, focus_window

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QMouseEvent
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


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
        icon_path, title_pattern, exe_path = apps[name]

        tile = AppTile(name, icon_path)
        layout.addWidget(tile)

        tile.clicked.connect(partial(launch_app, title_pattern, exe_path))

    button_exit = QPushButton("Exit the program")

    layout.addWidget(button_exit)

    button_exit.clicked.connect(window.close)
    button_exit.setFixedSize(110, 45)

    window.show()
    app.exec()


class AppTile(QWidget):
    clicked = pyqtSignal()

    def __init__(self, display_name, icon_path):
        super().__init__()
        self.setFixedSize(150, 180)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.set_tile_color(color="#292929")
        tile_layout = QVBoxLayout()
        self.setLayout(tile_layout)
        tile_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label = QLabel()
        icon_label.setPixmap(QIcon(icon_path).pixmap(48, 48))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tile_layout.addWidget(icon_label)
        text_label = QLabel()
        text_label.setText(display_name)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tile_layout.addWidget(text_label)

    def enterEvent(self, event):
        self.set_tile_color(color="#3A3A3A")

    def leaveEvent(self, event):
        self.set_tile_color(color="#292929")

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event is not None and event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

    def set_tile_color(self, color):
        self.setStyleSheet(
            f"AppTile {{background-color: {color}; border-radius: 12px;}}; QLabel {{ background-color: transparent; }}")


def launch_app(title_pattern, exe_path):
    hwnd = find_window(title_pattern)

    if hwnd is not None:
        focus_window(hwnd)
        return

    try:
        subprocess.Popen([exe_path])
    except OSError as e:
        QMessageBox.critical(None, "Launch Error", str(e))

if __name__ == "__main__":
    main()
