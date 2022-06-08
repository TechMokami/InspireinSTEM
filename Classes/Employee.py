#!/usr/bin/python

##################################
#       Subject: CLASSES
#       Name:    Joan Mokami
#       Date:    23/05/2022
##################################
##Assignment: Create a program to 
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    
    def sayHi(self):
        print('My name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old')
employee1=Employee('Jack', 20,000)
employee1.sayHi()
                                                                                                                                                                                                           
employee2=Employee('Jane'  ,50,000)
employee2.sayHi()
