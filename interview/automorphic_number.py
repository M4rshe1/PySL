# This file contains the solution for the Automorphism Number problem.
# A number is called Automorphism number if and only if its square ends in the same digits as the number itself.
def check_number(number):
    return str(number ** 2).endswith(str(number))
