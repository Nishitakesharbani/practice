people=30
cars=40
truck=15

if cars > people:
    print("We should take the car")
elif cars< people:
    print("We should not take the car")
else:
    print("We can't decide")

if  truck > cars :
    print("Thats too many truck")
elif truck < cars:
    print("Maybe we could take the truck")
else:
    print("We still can't decide")

if people> truck:
    print("Alright lets buy truck.")
else:
    print("Fine lets stay at home then")