import time, sys, timeit
from utils import delay_print

treeVisual = r"""
            [1]
        /    |      \
    [3]     [2]     [4]
   /    \
 [5]    [6]
"""
startingCode = """

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return
"""

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

root = Node(None, [Node(None, [Node(), Node()]), Node(), Node()])

def evaluate():
    result = 0
    while result != 3:
        line = input("> ")
        try:
            exec("def maxDepth(root: 'Node') -> int: return " + line, globals())
            delay_print("Running...")
            time.sleep(1)
            result = maxDepth(root)
        except:
            print(sys.exc_info())
    delay_print("Awesome work! That'll help us define optimal search paths when we're sending our drones out.")
    delay_print("They have pretty limited fuel, so it's important that we figure out which targets they can reach.")
    time.sleep(1)
    delay_print("You've been a big help!")
    return


def puzzle2():
    delay_print("You're crushing these problems so far. This one is a bit harder.")
    delay_print("We have a number of programs that run a form of depth-first search.")
    delay_print("Specifically, we want a quick program that will give us the maximum depth of a search tree.")
    delay_print(treeVisual)
    delay_print("For example, this tree would have a maximum depth of 3.")
    input("Press Enter to continue...")
    delay_print("We'll handle all the data processing for you; can you write a function to find the maximum depth?")
    delay_print(startingCode)
    evaluate()
    delay_print("Let's wrap up for the day. Great work, and I'll have something new prepared for you tomorrow!")
    return
