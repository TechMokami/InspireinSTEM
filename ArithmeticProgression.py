#!/usr/bin/python

#################################
#       Arithmetic Progression
#       Name: Joan Mokami
#       Date: 27/05/2022
#################################

# Formula =(a+(n-1)d)
# a=first term
# n=number of terms
# d=common difference

a=int(input("Enter the first number "))
n=int(input("Enter the number of terms "))
d=int(input("Enter the common differnce "))

for i in range(1,n+1):
    n_term=(a+(i-1)*d)
    s_n = (n_term/2)*(2*a+(n-1)*d)
    print(n_term)
print(s_n)
