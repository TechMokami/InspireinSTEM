#!/usr/bin/python

#######################
#       DICTIONARIES
#       Name: Joan Mokami
#       Date: 23/05/2022
#######################


# Initialising Dictionaries
Student={"Name":"Joan","Age":"18","Gender":"Female"}
# print(Student['Name'])
Student["ID No"]="10745433"
Student["Hobby"]="Cycling"
Student["Form"]="3"
# print(Student)

# # Initialising Empty Dictionaries
Student1={}
Student1["Fav food"]="Chapati"
Student1["Pet name"]="Leo"
# print(Student1)

#Modifying values
Student["Age"]="23"
# print(Student)

# Removing key value parts - use del()
del Student1["Fav food"]
# print(Student1)

                        # 25/05/2022
#DICTIONARIES - Collection of key value pairs
# Syntax : dictionary = {'key':'value'}
name = 'Joan Mokami'
colour = {'colour':'blue'}
vehicle = {'model':'Toyota','plate_number':'KDB 567Z'}
# type() - used to find the type of data structure
# print(type(colour))
# print(type(name))
# Accessing values inside a dictionary - using the KEY
# print(vehicle['model']) 
# print(vehicle['model'],vehicle['plate_number'])

#Dictionary - person
person = {
    'name':'John',
    'gender':'male',
    'ID_number':'1022364',
    'location':'kenya'
    }
#To add an element into a dictionary
person['age']='21'
person['fav colour']='blue'
# print(person)
# print(type(person))
# print(person['name'],person['age'],person['fav colour'])
# del person['ID_number']
# print(person)

#Get method to access a value in a dictionary.
# Method/in-built functions have a parenthesis-print()-Arguments go inside the parenthesis
# print(person.get('location','the location key is non-existent'))
# print(person.get('password','the \'location\' key is non-existent'))

# print(person.get('password','the \'location\' key is non-existent'))

#Task1
mary_fav_food=['beef','chicken','mushroom']
jane_fav_food=['ham','bacon','ugali']

fav_food={
    'mary':mary_fav_food,
    'jane':jane_fav_food
    }
print(fav_food)

#Task2
#Create a dictionary inside a dictionary
colours=['blue','pink','purple','yellow']
food=['ugali','rice','egg']
dictionary={'colours':colours,'food':food}
print(dictionary)