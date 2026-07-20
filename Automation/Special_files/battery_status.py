import psutil
from time import sleep
from plyer import notification
from .TTS_Fast import speak
import threading

def battery_alert_100():
    notification.notify(title = "Battery is full.", message_1 = "Unplug the charger.")

def battery_status(status):
    
    battery = psutil.sensors_battery()
    sleep(2)
    percentage = int(battery.percent)
    plugged = battery.power_plugged
    message_1 = f"Right now, battery percentage is {percentage}%"
    message_2 = "The laptop is plugged in."
    message_3 = "The laptop is not plugged in."

    if "battery percentage" in status:
        if percentage == 100:
            battery_alert_100()
        elif percentage >= 90 and percentage < 100:
            speak(message_1)
            print(f"Battery: {percentage}%")
            sleep(2)
            if plugged:
                speak(message_2)
            else:
                speak(message_3)
        elif percentage >= 80 and percentage < 90:
            speak(message_1)
            print(f"Battery: {percentage}%")
            sleep(2)
            if plugged:
                speak(message_2)
            else:
                speak(message_3)
        elif percentage >= 70 and percentage < 80:
            speak(message_1)
            print(f"Battery: {percentage}%")
            sleep(2)
            if plugged:
                speak(message_2)
            else:
                speak(message_3)
        elif percentage >= 60 and percentage < 70:
            speak(message_1)
            print(f"Battery: {percentage}%")
            sleep(2)
            if plugged:
                speak(message_2)
            else:
                speak(message_3)
        elif percentage >= 50 and percentage < 60:
            speak(message_1)
            print(f"Battery: {percentage}%")
            sleep(2)
            if plugged:
                speak(message_2)
            else:
                speak(message_3)
        elif percentage >= 20 and percentage < 50:
            speak(message_1)
            print(f"Battery: {percentage}%")
            sleep(2)
            if plugged:
                speak(message_2)
            else:
                speak(message_3)
        elif percentage >= 30 and percentage < 20:
            speak(message_1)
            speak("Your battery level is low connect to charger.")
            print(f"Battery: {percentage}")
        elif percentage <= 20 and not plugged:
            speak(message_1)
            speak("Your battery level is very low connect to charger.")
            print(f"Battery: {percentage}%")
        else:
            pass

if __name__ == "__main__":
    x = input()         
    battery_status(x)