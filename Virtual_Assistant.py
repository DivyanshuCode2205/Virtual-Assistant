from Automation.Automation_Brain import Auto_main_brain
from Automation.Special_files.internet_checker import internet_checker
from Speech_Listener import listen, get_Last_input
from time import sleep
import threading

def check_input():
    last_command = ""
    while True:
        command = get_Last_input().strip()
        sleep(0.1)
        if command and command != last_command:
            last_command = command
            print(f'Command: {last_command}')
            Auto_main_brain(last_command)
        else:
            pass

notifier_thread = threading.Thread(target=internet_checker, daemon=False)
listen_thread = threading.Thread(target=listen, daemon=True)
notifier_thread.start()
notifier_thread.join()
listen_thread.start()
listen_thread.join(timeout=7)

try:
    check_input()
except KeyboardInterrupt:
    print('Stop')
