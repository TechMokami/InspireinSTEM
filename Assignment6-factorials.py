#!/usr/bin/python
# Find the factorial of 6 and9
# Using for loop.
# num=int(input("Enter the number "))
# factorial=1
# for num in range(1,num+1):
#     factorial=factorial*num
# print(factorial)

# 
num=int(input('Enter a number '))

if num < 0:
    print("Factorial does not exist ")
elif num==0:
        print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=1
        factorial=factorial*i
        print("Factorial of the number is " + str(factorial))
print()