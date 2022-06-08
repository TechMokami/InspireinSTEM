#!/usr/bin/python

##################################
#       Subject: CLASSES
#       Name:    Joan Mokami
#       Date:    03/06/2022
##################################
class Person:
    def __init__(self, _name, _age):
        self.name=_name 
        self.age=_age
    
    def sayHi(self):
        print('Hello, my name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old')
person1=Person('Bob',16)
person1.sayHi()
                                                                                                                                                                                                           
person2=Person('James',22)
person2.sayHi()
