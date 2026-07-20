import webbrowser
import time
import pyautogui as gui

def play_music_spotify(song):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(5)
    gui.leftClick(542, 227) # opens search box
    gui.write(song) # enters song name in the search box
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(2)
    gui.leftClick(1389, 443) # clicks on play button

if __name__ == "__main__":
    s = input('song: ')
    play_music_spotify(s)
