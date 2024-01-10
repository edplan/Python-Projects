# Author: Eddi F. Miranda-Perez
# GitHub username: edplan
# Date: Apr. 06, 2022
# Description: The program will ask a user for an integer number
#              from 0 - 99 and output how many of each type of coin
#              would represent that amount with the fewest total number
#              number of coins. 

quarter = 25
dime = 10
nickle = 5
cent = 1

user_input = int(input("Please enter an amount in cents less than a dollar.\n"))

q = user_input // quarter
quarter_remainder = user_input % quarter

dime_remainder = quarter_remainder % dime
d = quarter_remainder // dime

nickle_remainder = dime_remainder % nickle
n = dime_remainder // nickle

penny_remainder = nickle_remainder % nickle
p = nickle_remainder // cent

print("Your change will be:\n" + "Q:", q, "\n" + "D:", d, "\n" + "N:", n, "\n" + "P:", p)

