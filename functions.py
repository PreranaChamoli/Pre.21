# working on functions
""""
def my_functions():
    print("hello")

my_functions()

def my_functions1(name):
    print(name)

    my_functions1("King")

def my_functions2(firstname, lastname):
    print(firstname, lastname)

my_functions2("king", "mark")

def my_functions3(*names):
    print(names)

my_functions3("king", "mark", "peter")

def add_all_numbers(*numbers):
    total = 0
    for number in numbers:
        total =total + number
        print(total)  
    return total

total_numbers = add_all_numbers(1,3,5,7) # take all inputs and put it in total

def list_all_properties(**car):
    the_input = car
    print(f'={car['maker']})
    for i in car.items():
        print(i)
    return car
properties = list_all_properties(maker = "Toyota", year = 2008, model = "corolla", colour = "yellow")


def my_functions_with_default(name="nick"):
    print(name)
my_functions_with_default("king")  

def dictionart_maker(**kwargs):#key word arguments
    return kwargs

    cars = dictionary_maker(maker = "Toyota", year = 2008, model = "corolla", colour = "yellow")
"""

def morning():
    return"good morning"

def afternoon():
    return "good afternoon"

def greeter():
    if time == "sunrise":
        return morning()
    elif time == "sunset":
            return afternoon()
    else:
            return"unknown time"   

#greater("sunset)"

def greeter2(fn):
    print("running function")
    print(fn())
    print ("finished running function")

    greeter2()
