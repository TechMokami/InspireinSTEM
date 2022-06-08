#LISTS Box brackets 9 #DICTIONARIES- Curly Brackets
 #TUPLES - Round brackets
 #they store multiple items in a single variable 12
#can be ordered and is unchangeable 13
#the built in data types that stor4e collections of data in one variable include 14
#list, set, dictionary, tuple

 #create a tuple
fruits = ("cherry", "banana", "grapes", "kiwi", "apple") 
print(fruits)

#accessing an item from a tuple using indexes 
print(fruits[1])

#Tuples are unchangeable, cannot be edited, added, removed once a tuple is created 
fruits[0]= "guava" #error

#finding how many items are in a tuple use (len)
print(len(fruits))

#finding the data structure
print(type(fruits))

#create a tuple using the tuple function
motorcycles = tuple( ("Ducati", "Harley", "Ninja", "Chopper")) 
print(motorcycles)

#Can consist of only one item but has to have a comma after it it to acknowledge it as a tuple
colors= ("violet",) 
print(type(colors))

for motorcycle in motorcycles: 
    print(motorcycle)

cars=("Audi","Tesla","BMW","Honda")
cars=("Mercedees","VW","Toyota","Mitsubishi")
print(cars)