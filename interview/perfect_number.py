def is_perfect_number(number):
    if number <= 0:
        return False
    summ = 0
    for i in range(1, number):
        if number % i == 0:
            summ += i
    return summ == number


input(is_perfect_number(int(input("Enter a number: "))))
