import time, sys, timeit
from utils import delay_print
from introduction import intro
from puzzle1 import puzzle1


def main():
    cash = 0
    player_name =  intro()
    cash = puzzle1(cash)
    cash += puzzle2(cash)

if __name__ == '__main__':
    main()
