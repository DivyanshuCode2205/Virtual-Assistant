import subprocess

def disable_chrome_microphone():
    subprocess.run(["taskkill", "/F", "/IM", "chrome.exe", "/T"],capture_output=True, text=True)

if __name__ == "__main__":
    disable_chrome_microphone()