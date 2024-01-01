# Author: Eddi F. Miranda-Perez
# GitHub username: edplan
# Date: Apr. 06, 2022
# Description: Asks the user for a temperature in celsius and
#              converts it to fahrenheit.

celsius = float(input("Please enter a Celcius temperature: "))
conversion = (celsius * 1.8) + 32
print("The equivalent Fahrenheit temperature is:\n" + str(conversion))
