from sys import exit

def gold_room():
    print("This room is full of gold. how much do you take")

    choice  = input("> ")
    if "0" in choice or "i" in choice:
        how_much= int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much<50:
        print("Nice you are greedy, you win")
        exit(0)
    else:
        dead("You gready bastard")

def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear")
    bear_moved=False

    while True:
        choice=input(">")
        if choice ==" take honey":
            dead("The looks at you then slaps you face off ")
        elif choice =="taunt bear":
            print ("The bear has movd from the room")
            print("You can go through it now")
            bear_moved=True
        elif choice== "taunt bear" and bear_moved:
            dead("the bear get piss of and chews your legs off")
        elif choice =="open door" and  bear_moved:
            gold_room()
        else:
            print("I got the idea what you mean")

def chthu_room():
    print("here you are the great evil")
    print("He, it , whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head")

    choice=input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well rhat was tasty")
    else:
        chthu_room()

def dead(why):
    print(why,"good job" )
    exit(0)

def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which one do you take")
    choice =input(">")
    if choice =="left":
        bear_room()
    elif choice =="right":
        chthu_room()
    else:
        dead("You stump around the room until you strave")

start()