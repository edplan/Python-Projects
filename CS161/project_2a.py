# Author: Eddi F. Miranda-Perez
# GitHub username: edplan
# Date: Apr. 06, 2022
# Description: Asks the user for five numbers and then 
# .............prints out the average of those numbers.

num_list = []

while len(num_list) != 5:
    print("Please enter 5 numbers: ")
    num1 = float(input())
    num_list.append(num1)
    
print(sum(num_list) / 5)