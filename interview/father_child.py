if __name__ == "__main__":
    total: int = int(input("Total age of father and child: "))
    before_time: int = int(input("How many years ago: "))
    times: int = int(input("How many times: "))
    for i in range(1, total):
        father_age: int = total - i
        if father_age - before_time == times * (i - before_time):
            print(f"Father age is {father_age} and child age is {i}")
            break
