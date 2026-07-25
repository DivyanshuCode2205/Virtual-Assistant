import pyautogui as gui # Programtically controls and automate mouse and keyboard
import time

def open_app(app):
    try:
        gui.press("win") # presses the windows key
        time.sleep(0.2)
        gui.write(app) # writes the name of app in seach box
        time.sleep(0.2)
        gui.press("enter") # presses enter key
    except Exception as e:
        print(f"Error happened with {app} app -> {e}")

if __name__ == "__main__":
    while True:
        x = input('App to open: ')
        open_app(x)