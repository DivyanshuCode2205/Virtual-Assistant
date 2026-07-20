import ctypes
from time import sleep

def lock_computer():
    sleep(3)
# LockWorkStation is Windows API for locking Work stations
    ctypes.windll.user32.LockWorkStation()

if __name__ == "__main__":
    lock_computer()