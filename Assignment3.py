#!/usr/bin/python

# If... else
# gender = input(" what is your gender : Male / Female ")
age = input("How old are you ? ")
account_balance = 0
if (int (age) > 25) and (int(age) < 30) : 
    account_balance=account_balance + 10000
    print("You have received a 10000 bonus")
else : 
    print("Sorry, no money for you ")


