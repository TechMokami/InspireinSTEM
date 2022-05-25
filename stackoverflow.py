#!/usr/bin/python

#######################
#       LOOPS : For Loop
#       Name: Joan Mokami
#       Date: 23/05/2022
#######################
print("Number \t Square")
print("================")
# for number in range(0,9):
# for number irange(1,9):
#         print(number)
#         print(number**2, end=" ")
# for number in range(start, end+ 1):
#     square = number**2
#     print(number, '\t', square)
# Get the starting value.
print('This program displays a list of numbers')
print('and their squares.')
start = int(input('Enter the starting number: '))

# Get the ending limit.
end = int(input('How high should I go? '))

# Print the table headings.
print()
print('Number\tSquare')
print('==============')


# Print the numbers and their squares.
for number in range(start , end+ 1):
    square = number**2
    print(number, end="")
    print(square, end="");print("\n")
    # print(square, end="");print("\n")

        

    

    




