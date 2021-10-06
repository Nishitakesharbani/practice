#create a mapping of state to apperviation
states={
    'oregon':'OR',
    'Florida':'Fl',
    'Califorina':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

#create a basic set of statement of states amd some cities in them
cities={
    'CA' : 'San Franosco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#add som more cities
cities['NY']="New york"
cities['OR']="Portland"

#print out some cities
print("_"*10)
print("Ny states has: ",cities['NY'])
print("OR states has: ",cities['OR'])

#print some states
print('_'*10)
print("Michingan appreviation is: ",states['Michigan'])
print("Florida appreviation is: ",states['Florida'])

# do it by using the states then cities dict
print('_'*10)
print("Michingan has is: ",cities[states['Michigan']])
print("Michingan has is: ",cities[states['Michigan']])

#print every state appreviation
print('_'*10)
for state, abbrev in list(states.items()):
    print(f"{states} is abbreviated {abbrev}")

#print every city in state 
print('_'*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the time 
print("_"*10)
for state, abbrev in list(states.items()):
    print(f"{states} is abbreviated {abbrev}")
    print(f"and has the {city[abbrev]}")

print("_"*10)
state=states.get('Texas')

if not state:
    print("Sorry, No Texas.")

#get a city with default value
city=cities.get('TX','Does not exist')
print(f"The city for this state 'TX' is: {city}")