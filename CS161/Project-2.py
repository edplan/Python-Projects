# Author: Eddi F. Miranda-Perez
# GitHub username: edplan
# Date: Apr, 06, 2022
# Description: Asks the user for five numbers and then 
# .............prints out the average of those numbers.

user_input1 = input("Please enter five numbers.")
user_input2 = input("Please enter five numbers.")
user_input3 = input("Please enter five numbers.")
user_input4 = input("Please enter five numbers.")
user_input5 = input("Please enter five numbers.")

sum_val = int(user_input1) + int(user_input2) + int(user_input3) + int(user_input4) + int(user_input5)

mean_val = sum_val / 5
print(mean_val)