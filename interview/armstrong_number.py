# Script to calculate if an input number is an armstrong number
# An armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits
def calculate_armstrong_number(number):
    summe = 0
    for i in str(number):
        summe += int(i) ** 3
    return summe == number


input(calculate_armstrong_number(input("Enter a number: ")))

