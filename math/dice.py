import random


def roll_dice(to_dice=6, dices=1) -> tuple:
    """
    Rolls a dice until the sum of the dices is equal to the given number.
    :param to_dice: What number should be diced?
    :param dices: How many dices should be rolled?
    :return: a tuple with the number of rolls and the sum of the dices
    """
    count = 0
    summed = 0
    while True:
        random_int = 0
        for i in range(int(dices)):
            random_int += random.randint(1, 6)

        summed += random_int
        count += 1
        if random_int == dices * to_dice:
            return count, summed


if __name__ == "__main__":
    result = roll_dice(
        int(input("What number do you want to roll?: ")),
        int(input("How many dices do you want to roll?:"))
    )

    print("Dice count: ", result[0])
    print("Summe: ", result[1])
