# Author: Eddi F. Miranda-Perez
# GitHub username: edplan
# Date: Apr. 06, 2022
# Description: The program will be promted how many integers they would like to enter
#              and the program will return the numbers in order from smallest to largest.


int_num = int(input("Cuantos numeros me quieres dar?"))

print("dame los", int_num, "numeros")

nums = []

while int_num > 0:
    user_nums = int(input())
    nums.append(user_nums)
    int_num -= 1 
max_val = 0
min_val = 0
for i in range(len(nums)-1, -1, -1):
    curr_num = nums[i]
    next_num = nums[i - 1]
    last_val = nums[-1]
    if curr_num == last_val:
        if curr_num < next_num:
            min_val = curr_num
        elif curr_num > next_num:
            max_val = curr_num
    if i >= 0:
        if curr_num < min_val:
            min_val = curr_num
        elif curr_num > max_val:
            max_val = curr_num
        
print("The minium value is: ", min_val )   
print("The maxumum value is: ", max_val )   
        



