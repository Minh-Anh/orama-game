import time, sys, timeit
from utils import delay_print

start = [0, 8, 3, 12, 1]
end = [0, 1, 3, 8, 12]

def end():
    time.sleep(5)
    delay_print("Still here?")
    time.sleep(2)
    delay_print("Doing some soul-searching, huh.")
    time.sleep(2)
    delay_print("Everyone gets to this point eventually. Well, almost everyone.")
    time.sleep(1)
    delay_print("I know it's probably not exactly what you wanted to be doing.")
    time.sleep(1)
    delay_print("But, you know, there aren't any perfect companies. They all do some things we don't agree with.")
    time.sleep(1)
    delay_print("It could be a lot worse.")
    time.sleep(5)
    delay_print("On a scale from 1 to 10, how comforted were you by those statements?")
    time.sleep(8)

def evaluate():
    result = start
    while result != end:
        line = input("> ")
        if(line == 'nvm'):
            break
        try:
            exec("q = lambda l: " + line, globals())
            delay_print("Running...")
            time.sleep(1)
            result = q(start)
        except:
            print(sys.exc_info())
        print("To go back, type 'nvm'")
    if(line != 'nvm'):
        delay_print("Damn. That's...genuinely quite impressive.")
        return True
    return False

def puzzle3():
    delay_print("You're up late! Couldn't sleep?")
    delay_print("That happens a lot.")
    time.sleep(1)
    delay_print("Looking for another problem to work on?")
    resp = input("> ")
    if('y' in resp):
        delay_print("Awesome! We're looking to deal with our sorting algorithm. Are you familiar with Quicksort?")
        delay_print("If not, go look it up. I'll just wait.")
        input("Press Enter to continue...")
        delay_print("Pretty straightforward, right? Can you write a one-line function for quicksort?")
        if(evaluate()):
            delay_print("I don't really have anything else for you.")
            end()
        else:
            delay_print("Don't work too hard. Burnout is real, and we care about you.")
            end()
    else:
        delay_print("Oh. I don't really know if I can help you then.")
        end()
