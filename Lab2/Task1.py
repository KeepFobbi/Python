num1 = float(input("Число 1: "))
num2 = float(input("Число 2: "))
procedure = input("Поддерживаемые операции: +, -, /, *, mod, pow, div\n>>>")



if procedure == '+':
    print(num1 + num2)
elif procedure == '-':
    print(num1 - num2)
elif procedure == '*':
    print(num1 * num2)
elif procedure == "mod":
    if num2 != 0:
        print(num1 % num2)
    else:
        print("Деление на 0!")
elif procedure == "pow":
    print(num1 ** num2)
elif procedure == "div":
    if num2 != 0:
        print(num1 // num2)
    else:
        print("Деление на 0!")
elif procedure == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Деление на 0!")