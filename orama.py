import time, sys, timeit
from utils import delay_print
from introduction import intro
from puzzle1 import puzzle1
from puzzle2 import puzzle2
from nights import night1
from puzzle3 import puzzle3
from playsound import playsound
import os
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

soundfile = os.path.join(application_path, 'sounds/ding.mp3')

def main():
    playsound(soundfile, False)
    time.sleep(1)
    player_name =  intro()
    cash = puzzle1(application_path)
    puzzle2()
    night1(application_path)
    puzzle3()


if __name__ == '__main__':
    main()
