import pywhatkit as pw # automates WhatsApp and Youtube

def play_on_yt(video_name):
    # opens browser and plays the most relevant result for search 'video_name'.
    pw.playonyt(video_name)

if __name__ == "__main__":
    x = input('video name : ')
    play_on_yt(x)