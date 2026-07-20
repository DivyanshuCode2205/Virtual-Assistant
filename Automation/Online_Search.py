import webbrowser
import pyautogui as gui
import pygetwindow as pgw
from time import sleep

link_1 = "https://youtube.com/"
link_2 = "https://google.com/"

def window():
    window = pgw.getActiveWindowTitle().strip().lower()
    if window is None:
        return None
    if "youtube" in window:
        return "youtube"
    elif "google drive" in window:
        return "google drive"
    elif "google" in window:
        return "google"
    elif "gmail" in window:
        return "gmail"
    elif "flipkart" in window:
        return "flipkart"
    elif "amazon" in window:
        return "amazon"
    elif "history" in window:
        return "history"
    elif "brave" in window:
        return "brave"
    
def universal_search(query):
    current_window = window()
    if current_window == "youtube":
        query = query.replace("search", "").strip().lower()
        gui.press("/")
        gui.write(query)
        sleep(1)
        gui.press("enter")
    elif current_window == "google":
        query = query.replace("search", "").strip().lower()
        gui.write(query)
        sleep(1)
        gui.press("enter")
    elif current_window == "google drive":
        query = query.replace("search", "").strip().lower()
        gui.press("/")
        sleep(0.2)
        gui.write(query)
        sleep(1)
        gui.press("enter")
    elif current_window == "gmail":
        query = query.replace("search", "").strip().lower()
        gui.press("/")
        gui.write(query)
        sleep(1)
        gui.press("enter")
    elif current_window == "amazon":
        query = query.replace("search", "").strip().lower()
        gui.hotkey("alt", "/")
        gui.write(query)
        sleep(1)
        gui.press("enter")
    # elif current_window == "flipkart":
    #     gui.leftClick(624, 313)
    #     gui.write(query)
    #     sleep(1)
    #     gui.press("enter")
    elif current_window == "history":
        query = query.replace("search", "").strip().lower()
        gui.write(query)
        sleep(1)
        gui.press("enter")
    elif current_window == "brave":
        query = query.replace("search", "").strip().lower()
        gui.hotkey("ctrl", "e")
        gui.write(query)
        sleep(1)
        gui.press("enter")
    else:
        query = query.replace("search", "").strip().lower()
        gui.write(query)
        sleep(1)
        gui.press("enter")

def clear_search():
    current_window = window()
    if current_window == "youtube":
        gui.press("/")
        gui.hotkey("ctrl", "a")
        gui.press("backspace")
        sleep(0.5)
        gui.leftClick(1505, 201)
    elif current_window == "google":
        gui.press("/")
        gui.hotkey("ctrl", "a")
        gui.press("backspace")
    elif current_window == "google drive":
        gui.press("/")
        gui.press("backspace")
        gui.press("esc")
        gui.press("esc")
    elif current_window == "gmail":
        gui.press("/")
        gui.press("backspace")
        gui.press("esc")
        gui.press("esc")
    elif current_window == "amazon":
        gui.hotkey("alt", "/")
        gui.hotkey("ctrl", "a")
        gui.press("backspace")
        gui.press("esc")
    # elif current_window == "flipkart":
    #     gui.leftClick(624, 313)
    #     gui.hotkey("ctrl", "a")
    #     gui.press("backspace")
    elif current_window == "brave":
        gui.leftClick(927, 86)
        sleep(0.5)
        gui.moveTo(1525, 119)
    elif current_window == "history":
        gui.hotkey("ctrl", "a")
        gui.press("backspace")

def youtube_search(query):
    webbrowser.open(link_1)
    sleep(1.5)
    gui.leftClick(1067, 210)
    gui.write(query)
    sleep(1)
    gui.press("enter")

def google_search(query):
    webbrowser.open(link_2)
    sleep(2)
    gui.leftClick(1144, 585)
    gui.write(query)
    sleep(1.5)
    gui.press("enter")