#CUbe and Sqauring
c_or_s = (input("Do you want to cube or square a number?(C or S): "))
if c_or_s == "C":
    number1 = int(input("What is the number you want to cube?"))
    calc_1 = (number1 ** 3)
    print(number1,"cubed is",calc_1)


elif c_or_s == "S":
    number2 = int(input("What is the number you want to square?"))
    calc_2 = (number2 ** 2)
    print(number2,"squared is",calc_2)


else:
    print("Invalit input")