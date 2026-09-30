import requests
from winotify import Notification, audio
from Automation.DATA.DLG_Data import dialogs_online, dialogs_offline
from random import choice
from Automation.Special_files.TTS_Fast import speak
import pyttsx3
import threading

run_online_dlg = choice(dialogs_online)
run_offline_dlg = choice(dialogs_offline)
    
def notifier(text):
    icon_path = r"D:\Pictures\Saved Pictures\gemini-svg.png"

    toast = Notification(
    app_id= "Virtual Assistant",
    title="",
    msg=text,
    duration="short",
    icon= icon_path
    )

    toast.set_audio(audio.Default, loop=False)

    # toast.add_actions(label="Click", launch="https://google.com/")
    # toast.add_actions(label="Dismiss", launch="https://github.com/")

    toast.show()

def offline_speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def is_Online(url = "https://google.com/", timeout = 5):
    try:
        response = requests.get(url, timeout = timeout)
        return response.status_code >= 200 and response.status_code < 300
    # covers both connection error and timeout
    except requests.exceptions.RequestException:
        return False

def internet_checker():
    if is_Online():
        t1 = threading.Thread(target=speak, args=(run_online_dlg, ))
        t1.start()
        t1.join()
        notifier(run_online_dlg)
    else:
        t2 = threading.Thread(target=offline_speak, args=(run_offline_dlg, ))
        t2.start()
        t2.join()
        notifier(run_offline_dlg)

if __name__ == "__main__":
    internet_checker()