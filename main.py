"""This module give us random dice
Author:Maryam Alavi
"""
import random


def roll_dice():
    """Simulate the rolling of a six-sided die.


    """
    dice_drawing = {
        1: (
            "-----",
            "| 1 |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "| 2 |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o 3|",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "| 4 |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| 5 |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o6o|",
            "|o o|",
            "-----",
        ),

    }
    roll = input("Roll the dice? (Yes/No) : ")
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        # The f before the string indicates that it's an f-string.
        print(f"dice rolled: {dice1} and {dice2}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes/no): ")


roll_dice()
