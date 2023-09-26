def calc(heads, legs, animal1, animal2):
    for i in range(heads+1):
        legs_total = i * animal1 + (heads - i) * animal2
        if legs_total == legs:
            return i, heads - i
    return 0, 0


if __name__ == "__main__":
    count_legs = input("Enter the number of total legs: ")
    count_heads = input("Enter the number of total heads: ")
    legs_animal1 = input("Enter the legs of animal 1: ")
    legs_animal2 = input("Enter the legs of animal 2: ")
    result = calc(int(count_heads), int(count_legs), legs_animal1, legs_animal2)
    input(f"There are {result[0]} of animal one and {result[1]} of animal two.")
