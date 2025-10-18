#Creating a calculator without tkinter
from time import sleep
print("Welcome to CALCULATOR :)")
Number_1 = int(float(input("What is the first number in your calculation? ")))
symbol = input("Choose your symbol, (+) (-)  (*)  (/)  ")
Number_2 = int(float(input("What is your second number ")))
if symbol == '+':
    print("Your7 answer is...")
    sleep(2)
    print(Number_1 + Number_2)
elif symbol == '-':
    print("Your answer is...")
    sleep(2)
    print(Number_1 - Number_2)
elif symbol == '*':
    print("Your answer is...")
    sleep(2)
    print(round(Number_1 * Number_2))
elif symbol == '/':
    print("Your answer is...")
    sleep(2)
    print(Number_1 / Number_2)
else:
    print("Invalid operator")