ten_things="Apple orange crows telephone light sugar"

print("Wait there are not  10 things in the list let's fix it ")
stuff= ten_things.split(' ')
more_stuff =("Day", "night", "song","frisbee","corn" ," Bananna"," girl", "Boy")

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print("Adding",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} item now")

print("There we go ",stuff)
print("Lets do some things with stuff")

print(stuff[1])
print(stuff[-1]) #whaao thats fancy
print(stuff.pop)
print(' '.join(stuff)) # whats thats cool
print('#'.join(stuff[3:5])) #super staler!