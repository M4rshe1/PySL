# Script to calculate if an input number is an armstrong number
def calculate_armstrong_number(number):
    summe = 0
    for i in str(number):
        summe = summe + int(i) ** 3
    return summe == number


input(calculate_armstrong_number(input("Enter a number: ")))

