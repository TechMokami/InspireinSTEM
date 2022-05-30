#!/usr/bin/python

#################################
#       Patterns
#       Name: Joan Mokami
#       Date: 27/05/2022
#################################

# Pattern of numbers using nested for loop
rows=int(input("Enter number of rows : "))
for i in range (rows):
    for j in range(i+1):
        print(j+1,end = " ")
    print("\n")