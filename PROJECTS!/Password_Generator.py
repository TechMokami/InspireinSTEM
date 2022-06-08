import random
print('Welcome to my password generator')
character='banana*999*$$'
num_passwords=int(input("How many passwords do you want? "))
len_password=int(input("How many characters should the password have? "))
print("\nHere are your passwords :")
for password in range(num_passwords):
    passwords=' '
    for c in range(len_password):
        passwords+=random.choice(character)
    print(passwords)
    #Generate a password using your phone number,email
    # Stores the user account and their password
    # Convert the code above into a class