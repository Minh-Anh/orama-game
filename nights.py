import time, sys, timeit
from utils import slow_print
from playsound import playsound

def night1(path):
    playsound(path + '/sounds/song.m4a', False)
    print("You close your laptop and head to bed.")
    time.sleep(3)
    print("It's been a good day. It seemed like they really liked you.")
    time.sleep(3)
    print("Already, you can hardly keep your eyes open.")
    time.sleep(3)
    print("Thoughts are running through your head but ", end='', flush=True)
    slow_print("gradually they evaluate as different expressions than if the condition were true then execute as needed")
    print("The plan was always to put in a couple of years ", end='', flush=True)
    slow_print("but it seemed like a long time yeah it seemed like maybe not the right time for making a change and with everything going on they saw an opportunity")
    print('why not')
    slow_print("there's always a path and the hardest path runs through the nicest places, so what if you didn't end up on that one, it's not a bad thing and no one can")
    print("You wake up.")
    time.sleep(3)
    print("Weird dreams.")
    time.sleep(3)
    print("You get a glass of water.")
    time.sleep(3)
    print("Back to bed.")
    time.sleep(6)
    print("Can't sleep.")
    time.sleep(5)
    print("Can't sleep.")
    time.sleep(3)
    print("Can't sleep.")
    time.sleep(1)
    print("You open your laptop.")
    return
