import time, sys, timeit
from utils import delay_print

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
