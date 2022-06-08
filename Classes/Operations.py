#!/usr/bin/python

##################################
#       Subject: CLASSES
#       Name:    Joan Mokami
#       Date:    23/05/2022
#       File:    Operations.py
##################################

from students import students


def add_numbers(x,y):
    result=x+y
    return result

def sub_numbers(x,y):
    result=x-y
    return result

def mult_numbers(x,y):
    result=x*y
    return result

def divide_numbers(x,y):
    result=x/y
    return result


new_student= students("Joan", "cycling","2003")
students.greet_student()
print(new_student)
