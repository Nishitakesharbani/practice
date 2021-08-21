def add(a,b):
    print(f"adding {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"subtracting {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"multipying {a} * {b}")
    return a*b

def divide(a,b):
    print(f"dividing {a} / {b}")
    return a/b

print("Lets do some maths with just function")
age=add(50,50)
height=subtract(100,20)
weight=multiply(15,4)
iq=divide(320,2)

print(f" Age :{age} height :{height} weight :{weight} IQ :{iq}")

print("Here is a puzzle")
what=add(age,subtract(height,multiply(weight,divide(iq,2))))
print(f"That becomes :{what}")