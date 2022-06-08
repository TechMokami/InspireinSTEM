
import numbers
from os import terminal_size
from platform import architecture


# formula=arn-1
# a=first_number
# r=common_ratio
# n=numberOfTerms
a=int(input("first number:"))
r=int(input("common ratio"))
n=int(input("number of terms"))

for i in range(1,n+1):
    n_term=(a*r)**(n-1)
    print(n_term)