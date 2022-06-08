# #!/usr/bin/python

# ###############################
# #       Subject:FUNCTIONS
# #       Name: Joan Mokami
# #       Date: 23/05/2022
# ###############################
# # It is a block of code that gets executed together

# #Initialising / defining a function
# def say_hello():
#     print("Hello Dani")

#     x=4
#     y=7
#     z=x+y
#     print(z)

# #Calling a function
# say_hello

# #Print a function of sounds made by some animals
# def bark():
#     print ("A dog barks.")
# bark()    

# def neigh():
#     print("A horse neighs.")
# neigh()

# def moo():
#     print("A cow moos.")
# moo()

# # Function parameters
# def add_numbers(x,y):
#     sum_of=x+y
#     print("The sum is ", sum_of)

# add_numbers(4,5)
# add_numbers(40,50)
# add_numbers(400,500)

# #Product of two numbers
# def prod(x,y):
#     prod=x*y
#     print("The product of the two numbers is ", prod)

# prod(60,30)
# prod(22,11)

#                         # 03/06/22
# # def print_name (name="Bob"):
# #     print(name)
# # print_name("Tom")


# #Return from a function
# # def get_sum(num1,num2):
# #     sum_nums=num1+num2
# #     return sum_nums
# # print(get_sum(7,12))

# #Write a function that gets the powers of numbers
# # def power(number,power):
# #     power_num=number**power
# #     return power_num
# # print(power(6,4))

# #Function to print ones full names
# # def get_fullname(f_name,s_name):
# #     full_name=f_name+ " " +s_name
# #     return full_name.title()
# # print(get_fullname("Mokami","Gichana"))


# Returning a dictionary from a function
def create_fullname(first_name,second_name):
    person={'first':first_name,'second':second_name}
    return person
student=create_fullname('Leah','Otieno')
print(student)

# Parsing a list in a function.
def greet_friends(names):
    for name in names:
        msg=("Hello " + name.title() + "!!")
        print(msg)
friends=['Eve','Joy','Dani','Sasha']
greet_friends(friends)