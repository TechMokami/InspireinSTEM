#!/usr/bin/python

##################################
#       Subject: CLASSES
#       Name:    Joan Mokami
#       Date:    23/05/2022
##################################

import Operations
from students import students
from teachers import Teachers

# print(Operations.add_numbers(4,5))
# print(Operations.sub_numbers(9,7))
# print(Operations.mult_numbers(5,4))
# print(Operations.divide_numbers(50,2))


# new_student= students("Joan", "cycling","2003")
# students.greet_student()
# print(new_student)

new_teacher = Teachers("John","773784","Math","50000")
new_teacher.get_tsc_no()
print(new_teacher.get_tsc_no())



