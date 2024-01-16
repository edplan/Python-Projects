# Author: Eddi F. Miranda-Perez
# GitHub username: edplan
# Date: Apr. 06, 2022
# Description: The program will ask a user for an integer number
#              from 0 - 99 and output how many of each type of coin
#              would represent that amount with the fewest total number
#              number of coins. 

# variables used to hold the values of the coins
quarter = 25
dime = 10
nickle = 5
cent = 1

# Asks user to enter an integer. Uses input function to store the value
user_input = int(input("Please enter an amount in cents less than a dollar.\n"))

# Calculate the amount of quarters used
q = user_input // quarter
# Calculate the remaining change
quarter_remainder = user_input % quarter

# Calculate the amount of dimes used
dime_remainder = quarter_remainder % dime
# Calculate the remaining change
d = quarter_remainder // dime

# Calculate the amount of nickles used
nickle_remainder = dime_remainder % nickle
# Calculate the remaining change
n = dime_remainder // nickle

# Calculate the amount of cents used
penny_remainder = nickle_remainder % nickle
# Calculate the remaining change
p = nickle_remainder // cent

print("Your change will be:\n" + "Q:", q, "\n" + "D:", d, "\n" + "N:", n, "\n" + "P:", p)

