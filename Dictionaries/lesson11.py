#!/usr/bin/python

############################################################################
#       Subject: Graphic User Interface - Using tkinter
#       Name:    Mokami Gichana
#       Date:    07/06/2022
#       File:    GUI_examples.py
############################################################################


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

#Looping over dictionaries - using for loops
colours = ['Blue','pink','purple']
for colour in colours:
    if colour=='Blue':
     print (colour.upper())

