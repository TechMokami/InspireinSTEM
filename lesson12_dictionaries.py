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
print(Student1)
