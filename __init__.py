# Python program for simple calculator

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1,  n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


select = int(input("select the operation 1/2/3/4 : "))

number_1 = int(input("Enter the number1 : "))

number_2 = int(input("Enter the number2 : "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", sub(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=", mul(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", div(number_1, number_2))
