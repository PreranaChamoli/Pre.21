# defining a list
myFruitlist = ["apple", "banana", "cherry"]
print(myFruitlist)
print(type(myFruitlist))


#Accesing list by position
print(myFruitlist[0]) 
print(myFruitlist[1]) 
print(myFruitlist[2]) 


# changing the value in a list
myFruitlist[2] = "orange"
print(myFruitlist)


# Introducting the tuple data type
myFinalAnswerTuple =("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))


# Accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Introducing the dictionary data type
myFavfruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo"  : "pineapple"
}
print(myFavfruitDictionary)
print(type(myFavfruitDictionary))


# Accessing a dictionary by name
print(myFavfruitDictionary["Akua"])
print(myFavfruitDictionary["Saanvi"])
print(myFavfruitDictionary["Paulo"])

for x in myFavfruitDictionary:
    print(x, ":", myFavfruitDictionary[x])
