
if __name__ == "__main__":
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    if first_number > second_number:
        smaller_number = second_number
    else:
        smaller_number = first_number
    for i in range(1, smaller_number + 1):
        if first_number % i == 0 and second_number % i == 0:
            greatest_common_divisor = i
    print(f"The greatest common divisor of {first_number} and {second_number} is {greatest_common_divisor}.")
    input("Press any key to exit.")
