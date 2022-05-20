# Lists
motorcycle_owner = "Mojo jojo"
plate_number = ['H103', 'Y120' ,'S650' , 'B777']
motorcycles = ['Honda','Yamaha','Suzuki']
# print(motorcycles)

# Accessing list items using indices
# print(motorcycles[0])

#Changing elements in a list
# # motorcycles[0] = "Bugatti"
# print(motorcycles[0])
# print("I love " + str(motorcycles[1]))

#Adding elements in a list
# motorcycles.append('Bugatti Yomaha') # Only one element can be added to the list #
# print(motorcycles)

#Removing elements from a list
#task-print each motorcycle with their plate number
# print(motorcycles[0],plate_number[0])
# print(MetavarType
# print(motorcycles[1],plate_number[1])
# print(motorcycles[2],plate_number[2])
# print(motorcycles[3],plate_number[3])

#deleting an element from a list
# del motorcycles[0]
# print(motorcycles)

# Pop method
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print (popped_motorcycle)
#  Task - print a statement 'My name is Mojo jojo and I own a motorcycle plate number ...'
# print("My name is {} and I own a motorcycle plate number {} " .format(motorcycle_owner, plate_number[0]))
# print(f"My name is {motorcycle_owner} and I own a motorcycle plate number {plate_number[0]}")
print(f"My name is {motorcycle_owner} and I own a {motorcycles[0]} motorcycle plate number {plate_number[0]}")

# Extracing an item from a list
motorcycles.remove('Honda')
print(motorcycles)