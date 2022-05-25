#!/usr/bin/python

############################
#       Assignment 4
#       Name: Joan Mokami
#       Date: 24/05/2022
############################

(account_balance) = input("Enter your account balance")
if (int(account_balance) > 100000) and (int(account_balance) < 2000000) :
    (account_balance) = int(account_balance) - 25000 
    print("Sh 25000 deducted from your balance") 
elif (float(account_balance) > 500000) and (float(account_balance) < 1000000) :
    (account_balance) = float(account_balance) - (0.3 * float(account_balance))
    print(account_balance)
    print("30% from your account has been deducted")
elif (account_balance > 1000000) :
    (account_balance) = int(account_balance) - 15000
    print("15000 deducted from your account")
else :
    print("No deduction done")
    