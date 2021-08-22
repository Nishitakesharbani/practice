print("""you enter a dark room with two doors
do ou go through door #1 or #2?""")
doors=input(">")
if doors =="1":
    print("""There is a gaint bear eating acheese cake
    what would you do?
    1. Take the cheese cake
    2. screams on the bear""")
    bear=input(">")
    if bear=="1":
        print("The ears eat of your face, Goodjob")
    elif bear=="2":
        print("The bear eats of your legs")
    else:
        print(f"Well doing {bear} is probaly better,")
        print("Bear ran away")

elif doors=="2":
        print("""You stare into endless abyss at chylhu,s return
              1. blueberries 
              2. yellow jacket
              3.understading revoles yelling melodies""")
        insanity=input(">")

        if insanity=="1" or insanity=="2":
            print("Your body survies powered by a wind of jello")
            print("god job")

        else:
            print("The insanity roots your eyes into a pool of muck.")
            print("Gooodjob")

else:
    print("You stumble around and fall on a knife and die. goodjob")