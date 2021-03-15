import time, sys

def delay_print(s, endl=True):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.01)
    if endl:
        print()

def slow_print(s, endl=True):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.1)
    if endl:
        print()
