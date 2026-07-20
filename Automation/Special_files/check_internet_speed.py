from speedtest import Speedtest
from .TTS_Fast import speak

def check_internet_speed():
    try:
        internet_speed = Speedtest()
        internet_speed.get_best_server()
        download_speed = internet_speed.download() / 1000000
        download_speed = round(download_speed, 2)
        upload_speed = internet_speed.upload() / 1000000
        upload_speed = round(upload_speed, 2)
        # ping = internet_speed.results.ping

        speak(f"Your download speed is {download_speed} Mbps and upload speed is {upload_speed} Mbps")
        print(f"Download speed: {download_speed} Mbps and Upload speed: {upload_speed} Mbps")
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        return ""

if __name__ == "__main__":
    s = check_internet_speed()
    print(s)