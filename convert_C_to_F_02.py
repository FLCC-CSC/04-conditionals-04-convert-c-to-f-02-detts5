# FILE NAME - convert_C_to_F_01.py

# NAME:Dan Dettman 
# DATE: 3/16/26
# BRIEF DESCRIPTION:This program converts a temperature
# from Celsius to Fahrenheit.

def convert_C_to_F():
    celsius = float(input("Enter a temperature in Celsius: "))
    
    fahrenheit = celsius * 9 / 5 + 32
    
    print()
    print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")

convert_C_to_F()  





#1. means a floating-point number that can contain decimals.





#2. Why do you think it is important to use `float` as opposed to
#a different type of variable type? because temperature values  are not always whole numbers.
