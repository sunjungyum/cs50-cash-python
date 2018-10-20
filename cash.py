# Sun-Jung Yum
# Problem Set 6
# 25 October 2018

from cs50 import get_float

while True:
    # Prompts user for change owed
    change = get_float("Change owed: ")

    # Breaks out of loop if change owed is valid (between 1 and 8, inclusive)
    if change >= 0.0:
        break

change = round(change * 100)

# Checks how many quarters and adds to numberOfCoins
numberOfCoins = change // 25
change = change % 25

# Checks how many dimes and adds to numberOfCoins
numberOfCoins += change // 10
change = change % 10

# Checks how many nickles and adds to numberOfCoins
numberOfCoins += change // 5
change = change % 5

# The remaining amount is added to numberOfCoins
numberOfCoins += change

print(numberOfCoins)