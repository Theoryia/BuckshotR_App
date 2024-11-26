from pyfiglet import Figlet
import alive_progress
import time
import random
import os

f1 = Figlet(font='larry3d')
f2 = Figlet(font='smslant')
f3 = Figlet(font='contessa')

items = ["phone", "adrenaline", "handcuffs", "beer", "cigarettes", "inverter", "saw"]
tube = []

def live_odds(blank, live):
    total_count = blank + live
    return (blank / total_count) * 100 if total_count > 0 else 0

def main():
    game()

def game():
    print(f1.renderText('Buckshot Roulette'))
    print(f2.renderText('starting'))
    time.sleep(0.2)
    with alive_progress.alive_bar(3500, bar='smooth') as bar:
        for i in range(3500):
            time.sleep(0.00002)
            bar()

    Continue = True
    while Continue:
        shotguntube()
        print(f3.renderText("Do you want to play again?"))
        res = input("y/n")
        if res.lower() == "n":
            Continue = False

def what_items():
    print(f3.renderText("Speak"))
    result = input(": ")
    if result and result[0].isdigit():
        words = result.split()
        if len(words) > 1:
            set_tube_state(result)
        else:
            print("?")
            time.sleep(1)
            what_items()
    elif result.lower() in ["no", "n"]:
        return
    else:
        print("?")
        time.sleep(1)
        what_items()

    print(f3.renderText("Done?"))
    done = input(": ")
    if done.lower() == "y":
        print(f3.renderText(" "))
        return
    else:
        what_items()

def set_tube_state(loc):
    tube[int(loc[0]) - 1] = "live" if "live" in loc else "blank" if "blank" in loc else "Unknown"

def decision(blank, live):
    what_items()
    p = live_odds(blank, live)
    print(p)
    if tube[0] == "Unknown":
        if p == 100:
            print(f2.renderText("Its a blank"))
        elif 95 < p < 100:
            print(f2.renderText("I bet its a blank"))
        elif 90 < p <= 95:
            print(f2.renderText("Very high chance its a blank"))
        elif 80 < p <= 90:
            print(f2.renderText("Probably a blank"))
        elif 70 < p <= 80:
            print(f2.renderText("Should be a blank"))
        elif 60 < p <= 70:
            print(f2.renderText("Might be a blank"))
        elif 50 < p <= 60:
            print(f2.renderText("Even but favouring a blank"))
        elif 40 < p <= 50:
            print(f2.renderText("Even but favouring a live"))
        elif 30 < p <= 40:
            print(f2.renderText("Probably a live"))
        elif 20 < p <= 30:
            print(f2.renderText("Very likely a live"))
        elif 10 < p <= 20:
            print(f2.renderText("Almost certain its a live"))
        elif p == 0:
            print(f2.renderText("Its a live round"))
        else:
            print("idk")
    elif tube[0] == "live":
        print(f2.renderText("Don't look down the barrel..."))
    elif tube[0] == "blank":
        print(f2.renderText("It's a blank..."))
    print("Next in the tube : ",tube[1])
    time.sleep(1)

    time.sleep(5)
    tube.pop(0)
    res = input(f3.renderText("Was it a Live or Blank? "))
    if res.lower() == "l":
        live -= 1
    elif res.lower() == "b":
        blank -= 1
    else:
        print("Invalid input")

    return blank, live

def shotguntube():
    print(f2.renderText("How many shells?"))
    total_shells = int(input(": "))
    print(f2.renderText("How many are live?"))
    live = int(input(": "))
    blank = total_shells - live
    for i in range(total_shells):
        tube.append("Unknown")
    print(live + blank)
    while live + blank > 0:
        blank, live = decision(blank, live)

if __name__ == "__main__":
    main()
