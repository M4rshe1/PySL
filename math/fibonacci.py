# Fibonacci sequence with recursion
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         print(n)
#         return fib(n - 1) + fib(n - 2)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, b + a
    print()


fib(int(input("How many do you want? \n>> ")))
