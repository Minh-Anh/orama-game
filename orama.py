import time, sys, timeit

arr1 = [0] * 1000
arr2 = [0] * 1000
arr1[0] = 1
arr1[1] = 3
arr2[1] = 2
arr2[2] = 10
d1 = {'a': 1, 'b':3}
d2 = {'b':2, 'c':10}

denseVectorDotProductExpanded = """
def dotProduct(arr1, arr2):
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum
"""
denseVectorDotProduct = """
def dotProduct(arr1, arr2):
    return sum(arr1[i] * arr2[i] for i in range(len(arr1)))
"""

sparseVectorDotProductEmpty = """
def dotProduct(d1, d2):
    return
"""

def delay_print(s, endl=True):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.01)
    if endl:
        print()

def introduction():
    delay_print("Welcome to Orama! You're one of the best and brightest of all the engineers we've interviewed.")
    delay_print("We're so excited that you're joining us to change the world.")
    input("Press Enter to continue...")
    delay_print("First of all, what's your preferred name?")
    delay_print("If you want to use your legal name, that's fine too, but we love nicknames here!")
    return input("> ")

def NPS():
    response = input("> ")
    while not response.isdigit():
        response = input("Please enter a number from 0 to 10. > ")
    NPS = int(response)
    if(NPS > 5):
        delay_print("Thanks for your feedback!")
    else:
        delay_print("Ouch. Well, thanks for your feedback.")

def evaluate():
    result = 0
    while result != 6:
        line = input("> ")
        try:
            result = eval(line)
        except:
            print(sys.exc_info())
    timeDense = timeit.timeit("sum(arr1[i] * arr2[i] for i in range(len(arr1)))", number=10000, globals=globals())
    timeSparse = timeit.timeit(line, number=10000, globals=globals())
    delay_print("Nicely done!")
    delay_print(f"Your code ran 10000 times in {timeSparse} seconds, versus {timeDense} seconds for our old code.")
    delay_print(f"That's a {100*(timeDense/timeSparse)}% improvement!")
    return timeDense//timeSparse


def puzzle1(cash):
    delay_print("Let's get to work, then. We're revamping some of our internal tooling right now.")
    delay_print("In order to perform linear regression efficiently, we need to be able to take dot products of sparse vectors quickly.")
    delay_print("Right now, our vectors are defined as arrays, and we iterate through each term to multiply them and add to get the dot product:")
    delay_print(denseVectorDotProductExpanded)
    input("Press Enter to continue...")
    delay_print("One of our engineers already rewrote it to be a one line function, like this:")
    delay_print(denseVectorDotProduct)
    delay_print("This is more concise, but it's not any faster; it's still iterating through a bunch of 0 terms.")
    delay_print("A better representation would be using a dictionary to represent a sparse vector, with 0 terms having no key mapped to them.")
    input("Press Enter to continue...")
    delay_print("Let's say we pass in two dicts, and we want to use a one line function to get their dot product.")
    delay_print(sparseVectorDotProductEmpty)
    delay_print("Fill in the expression after the return with a one line function for the dot product.")
    result = evaluate()
    delay_print("Here at Orama, we give out bonuses to our top performers.")
    delay_print("Since you did so well with that, here's a little something from us.")
    cash += result
    print()
    print(f"You got ${result}0! You now have ${cash}0.")
    return cash

def main():
    cash = 0
    player_name =  introduction()
    delay_print(f"Nice to meet you, {player_name}! I'm Clark, and I'll be helping you get set up.")
    delay_print("If you have any questions, please hesitate to ask me! I'm a very limited AI and I will not be helpful.")
    input("Press Enter to continue...")
    delay_print("Let me show you to your desk.")
    time.sleep(2)
    delay_print("Just kidding, we all work from home now. Ha ha! Just a little humor to make you feel more comfortable.")
    input("Press Enter to continue...")
    delay_print("On a scale from 0 to 10, how likely is it that you would recommend that joke to a friend or colleague?")
    NPS()
    input("Press Enter to continue...")
    cash = puzzle1(cash)

if __name__ == '__main__':
    main()
