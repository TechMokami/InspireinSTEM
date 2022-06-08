#!/usr/bin/python

##################################
#       Subject: CLASSES
#       Name:    Joan Mokami
#       Date:    23/05/2022
#       File:   teachers.py
##################################

f = open("lesson.txt")
f = open("lesson1.txt",)

#reading the file
# print(f.read())
# f.close()

#opening file
# with open ("lesson1.txt",'w') as f:
#     f.write("This is a file I made\n ")
#     f.write("On a monday morning \n") 
#     f.write("In the IYSP class. \n")
# print(f.read())
# f.close()

f= open("lesson1.txt")
print (f.readline())
'''
with open ("lesson1.txt",'w') as f:
    f.write("This is a file I made\n")
    f.write("\nOn a monday morning") 
    f.write("In the IYSP class.\n")
'''
print (f.read())
