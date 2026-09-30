import pyautogui as gui
import pygetwindow as pgw
from time import sleep

def detect_window():
    active_window = pgw.getActiveWindowTitle()
    
    if active_window is None:
        return None
    
    active_window = active_window.strip().lower()

    if "youtube" in active_window:
        return "youtube"
    
    elif "spotify" in active_window:
        return "spotify"

    elif "media viewer" in active_window:
        return "telegram"
    else:
        pass

def media_pause():
    current_window = detect_window()
    if current_window == "youtube":
        gui.press("k")
    elif current_window == "spotify":
        gui.press("playpause")
    elif current_window == "telegram":
        gui.press("k")
    else:
        pass

def media_resume():
    current_window = detect_window()
    if current_window == "youtube":
        gui.press("k")
    elif current_window == "spotify":
        gui.press("playpause")
    elif current_window == "telegram":
        gui.press("k")
    else:
        pass

"""def move_forward():
    current_window = detect_window()

    if current_window == "youtube":
        gui.press("l")
    elif current_window == "spotify":
        gui.hotkey("shift", "right")
    else:
        pass

def move_backward():
    current_window = detect_window()

    if current_window == "youtube":
        gui.press("j")
    elif current_window == "spotify":
        gui.hotkey("shift", "left")
    else:
        pass"""

def next_track():
    current_window = detect_window()
    if current_window == "youtube":
        gui.hotkey("shift", "n")
    elif current_window == "spotify":
        gui.press("nexttrack")
    else:
        pass

def previous_track():
    current_window = detect_window()
    if current_window == "youtube":
        gui.hotkey("shift", "p")
    elif current_window == "spotify":
        gui.press("prevtrack")
    else:
        pass

def music_brain_control(control_command):
    control_command = control_command.strip().lower()

    if "pause" in control_command or "stop" in control_command:
        media_pause()
    
    elif "resume" in control_command or "continue" in control_command or "unpause" in control_command or "play" in control_command:
        media_resume()
    
    elif "next track" in control_command or "play next" in control_command:
        next_track()
    
    elif "previous track" in control_command or "play last" in control_command:
        previous_track()

if __name__ == "__main__":
    x = input()
    music_brain_control(x)