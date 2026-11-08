import win32con
import win32gui
import pywintypes

def check_window(hwnd, search_data):
    title = win32gui.GetWindowText(hwnd)
    target = search_data["title_pattern"]

    matches = title == target if target == "Steam" else target in title

    if matches and "Overlay" not in title and win32gui.IsWindowVisible(hwnd):
        search_data["hwnd"] = hwnd

    return True


def focus_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    try:
        win32gui.SetForegroundWindow(hwnd)
    except pywintypes.error:
        print("Failed to focus window")

def find_window(title_pattern):
    search_data = {
        "title_pattern": title_pattern,
        "hwnd": None
    }

    win32gui.EnumWindows(check_window, search_data)

    return search_data["hwnd"]