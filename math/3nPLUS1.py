def plus(n, count):
    print(n)
    # print(count)
    count += 1  # Increment the count by 1
    if n == 1:
        return count
    if n % 2:
        n = n * 3 + 1
    else:
        n = n / 2
    return plus(n, count)


if __name__ == '__main__':
    c = 0
    print(plus(23, c))
