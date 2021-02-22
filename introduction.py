from utils import delay_print
import time

def NPS():
    response = input("> ")
    while not response.isdigit():
        response = input("Please enter a number from 0 to 10. > ")
    NPS = int(response)
    if(NPS > 5):
        delay_print("Thanks for your feedback!")
    else:
        delay_print("Ouch. Well, thanks for your feedback.")

def intro():
    delay_print("Welcome to Orama! You're one of the best and brightest of all the engineers we've interviewed.")
    delay_print("We're so excited that you're joining us to change the world.")
    input("Press Enter to continue...")
    delay_print("First of all, what's your preferred name?")
    delay_print("If you want to use your legal name, that's fine too, but we love nicknames here!")
    player_name = input("> ")
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
    return player_name
