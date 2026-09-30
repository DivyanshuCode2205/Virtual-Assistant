from .Web_Open import web_open
from .Open_App import open_app
from .music_play_yt import play_on_yt
from .Play_music_Spotify import play_music_spotify
from .media_control import music_brain_control
from .Online_Search import youtube_search, google_search, universal_search, clear_search
from .Tab_Automation import perform_browser_action
from .Special_files.lock_computer import lock_computer
from .Special_files.Restart_computer import restart_computer
from .Special_files.Disable_chrome_microphone import disable_chrome_microphone
from .Special_files.battery_status import battery_status
from .Special_files.check_internet_speed import check_internet_speed
from .Special_files.TTS_Fast import speak
from time import sleep
import pyautogui as gui
from Speech_Listener import get_Last_input

def open_brain(query):
    if "website" in query or "go to" in query:
        query = query.replace("open", "").strip()
        query = query.replace("website", "").strip()
        query = query.replace("go to", "").strip()
        sleep(0.2)
        web_open(query)
    else:
        query = query.replace("open", "").strip()
        query = query.replace("app", "").strip()
        open_app(query)

def closing_window():
    sleep(0.5)
    gui.click()
    gui.hotkey("alt", "f4")

def Auto_main_brain(request):
    request = request.strip().lower()
    if request.startswith("open") or request.startswith("go to"):
        open_brain(request)

    elif request.startswith("play music on spotify"):
        speak("Which music you want to play ?")
        sleep(0.5)
        print("Give name: ")

        old = get_Last_input().strip().lower()
        while True:
            new = get_Last_input().strip().lower()
            if new and new != old:
                x = new
                break
        sleep(0.5)
        play_music_spotify(x)

    elif request.startswith("play music on youtube"):
        prompt_reject = "which music you want to play"
        speak("Which music you want to play ?")
        # sleep(2)
        print("Give name:")
        sleep(2)
        old = get_Last_input().strip().lower()
        while True:
            sleep(0.3)
            new = get_Last_input().strip().lower()
            if new and new != old and prompt_reject not in new:
                y = new
                break
        sleep(2)
        play_on_yt(y)

    elif "search on google" in request or "i want to search on google" in request:
        prompt_reject = "what do you want to search on google"
        speak("What do you want to search on google ?")
        sleep(1.75)
        print("Query: ")
        # sleep(5)

        old = get_Last_input().strip().lower()
        while True:
            sleep(0.3)
            new = get_Last_input().strip().lower()
            if new and new != old and prompt_reject not in new:
                a = new
                break
        sleep(1)
        google_search(a)

    elif "search on youtube" in request or "i want to search on youtube" in request:
        prompt_reject = "what do you want to search on youtube"
        speak("What do you want to search on youtube ?")
        sleep(1)
        print("Query: ")

        old = get_Last_input().strip().lower()
        while True:
            sleep(0.3)
            new = get_Last_input().strip().lower()
            if new and new != old and prompt_reject not in new:
                b = new
                break
        sleep(0.5)
        youtube_search(b)

    elif request.startswith("search"):
        universal_search(request)
    
    elif request.startswith("clear"):
        clear_search()

    elif request == "close the tab" or request == "tab close karo":
        perform_browser_action(request)

    elif any(word in request for word in ["private window kholo", "switch to private window", "turn on incognito", "go incognito" "aage jao", "go forward", "piche jao", "go back", "history kholo", "show history", "previous tab per jao", "switch to previous tab", "next tab per jao", "switch to next tab", "refresh", "page refresh karo", "refresh the page", "zoom out karo", "zoom out", "zoom in karo", "zoom in", "browser menu kholo", "get browser menu", "tab band karo", "create new tab", "open new tab", "new tab kholo"]):
        perform_browser_action(request)

    elif any(word in request for word in ['play', 'resume', 'continue', 'pause', 'stop', 'next track', 'next song', 'previous track', 'last song']):
        music_brain_control(request)
    
    elif ("battery percentage" in request or "check battery" in request):
        sleep(1)
        prompt_reject = "right now battery percentage is"
        if prompt_reject not in request:
            battery_status(request)
    
    elif "check internet speed" in request or "check the internet speed" in request:
        check_internet_speed()
    
    elif request.startswith("lock"):
        lock_computer()

    elif "restart the computer" in request or "reboot the computer" in request:
        restart_computer()
    
    elif ("turn off the microphone" in request or "turn off the mic" in request or "mic off" in request):
        disable_chrome_microphone()

    elif request.startswith("close") or request.startswith("close the window"):
        closing_window()

    else:
        pass

if __name__ == "__main__":
    while True:
        x = input()
        Auto_main_brain(x)