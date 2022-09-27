# working with string data types
myString = "This is my string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

# working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#working with input strings
name = input ("what is your name? ")
print(name)

# Formatting output Strings
color = input("What is your favourite color? ")
animal = input("what is your favourite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))