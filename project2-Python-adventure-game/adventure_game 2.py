import time
import random
items = []
#my function definitions
def print_sleep(thing_to_print):
    print(thing_to_print)
    time.sleep(2)
def intro():
    print_sleep("On your way home from an event you get lost...")
    print_sleep("You find yourself in a very dark forest...")
    print_sleep("In front of you are three passageways.")
    print_sleep("You see an abandoned house on the first passageway,")
    print_sleep("you hear a strange sound from the second passageway")
    print_sleep("and you can hear a bus from the third passageway")

def begining():
    print_sleep("1.Do you want to see if there is help waiting at the abanndoned house?")
    print_sleep("2.Do you want to see what that noise was?")
    print_sleep("3.Or do you want to go to the bus?")
    print_sleep("Through passageway do you want to go?")
def random_champion():
    champion_list = ["good Job","great...Sherlock","superbb you made it","congratulation"]
    print_sleep(random.choice(champion_list))

def lost_play_again():
    print_sleep("You died!!!")
    print_sleep("Game Over...")
    print_sleep("Would you like to play again?")
    answer = input("please enter y/n\n")
    if answer == "y":
        game()
    elif answer == "n":
        exit()
    else:
        print_sleep("I dont understand...")
def passageway_1():
    print_sleep("You walk up to the house...")
    if "key" in items:
        print_sleep("You put your key in the lock")
        print_sleep("and it openend, yaaaaay")
        print_sleep("everything was full spiderwebs and dust")
        print_sleep("you walk around and find a sparkly blue paper")
        print_sleep("you than descide to take it with you")
        print_sleep("than you go back")
        items.append("ticket")
    elif "key" not in items:
        print_sleep("you go up to door to see...")
        print_sleep("the door is locked.")
        print_sleep("You try breaking the door, but the ghosts from the house attack you!")
        lost_play_again()
def passageway_2():
    if "key" not in items:
        print_sleep("As you are walking down the passageway, the odd sound begins to fade")
        print_sleep("and instead you see a shiny teasure box appear!")
        print_sleep("You open it and find a key.")
        print_sleep("You decide to take the key with you and go back")
        items.append("key")
    elif "key"  in items:
        print_sleep("You decide to return")
        print_sleep("It was a really bad idea...")
        print_sleep("The noise that has returned turns out to be a wolf's howl!")
        answer = input("What do you do? Type 1 to run and 2 to act dead!\n")
        if answer == "1":
            print_sleep("You run as fast as you could, but the wolf is faster...")
            print_sleep("He eats you and you die!")

            lost_play_again()
        elif answer == "2":
            print_sleep("You act dead, but the wolf is hungry...")
            print_sleep("It eats you and you die...")
            lost_play_again()
def passageway_3():
    if "ticket" in items:
        print_sleep("you give the ticket to the bus diver")
        print_sleep("he dropped you of at the main station")
        print_sleep("from where you went home")
        random_champion()
        print_sleep("You made it,congratulation!!!!!")
        print_sleep("Do you want to play again? ")
        answer=input("please answer with y/n\n")
        if answer == "y":
            game()
        elif answer == "n":
            exit()
        else:
            print_sleep("I dont understand...")
            answer=input("please answer with y/n\n")
            if answer == "y":
                game()
            elif answer == "n":
                exit()

    else:
        print_sleep("The bus driver would have taken cash to take you with him,")
        print_sleep("but because of Covid-19 he is not allowed to take cash.")
        print_sleep("You find yourself before the three passageways again...")
def game():
    intro()
    while True:
        begining()
        passageway = input("Please enter 1, 2 or 3 \n")
        if passageway == "1":
            passageway_1()

        elif passageway == "2":
            passageway_2()

        elif passageway == "3" :
            passageway_3()

game()
