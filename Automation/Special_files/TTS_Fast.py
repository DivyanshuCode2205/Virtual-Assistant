import os # to create and remove file
import subprocess # python runs command in terminal and give back the results
import tempfile # helps to create temporary files
from playsound import playsound
import threading
import sys

def play_then_delete(audio_file):
    playsound(audio_file) # blocking call by default
    os.remove(audio_file) # removes the file

# for hindi male voice -> hi-IN-MadhurNeural
# for hindi female voice -> hi-IN-SwaraNeural
def speak(text : str, voice : str = 'en-CA-LiamNeural') -> None:
    try:
        with tempfile.NamedTemporaryFile(delete = False, suffix = '.mp3') as temp_file:
            output_file = temp_file.name
        
        # terminal command that converts the given text to audio using selected voice
        # saves it to output_file.
        command = [
            sys.executable,
            "-m",
            "edge_tts",
            "--voice",
            voice,
            "--text",
            text,
            "--write-media",
            output_file
        ]
        # runs the given command in terminal
        subprocess.run(command, shell = True, check = True) # check=True if command fails then it will raise error immediately.

        # target=play_then_delete -> run this function in the background
        # args=(output_file,) -> pass this as its input of the function
        threading.Thread(target=play_then_delete, args=(output_file,)).start()

    except Exception as e:
        print(f"Error : {e}")
    

if __name__ == "__main__":
    while True:
        try:
            t= input('Text command: ')
            speak(t)
        except KeyboardInterrupt:
            print('Terminating the program ....')
            break
