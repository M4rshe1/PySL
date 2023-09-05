# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, b + a
#     print()

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, b + a
    print()


fib(int(input("How many do you want? : ")))
