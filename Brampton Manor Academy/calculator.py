def calculator():
    information = str(input("Enter your calculation or enter q to quit: "))

    if information.lower() == 'q':
        return

    string = information.split(" ")
    number_1 = int(string[0])
    number_2 = int(string[1])
    operation = string[2]

    if operation == '+':
        result = number_1 + number_2
        print(result)
    elif operation == '-':
        result = number_1 - number_2
        print(result)
    elif operation == '*':
        result = number_1 * number_2
        print(result)
    elif operation == '/':
        result = number_1 / number_2
        print(result)
    elif operation == '//':
        result = number_1 // number_2
        print(result)
    elif operation == '%':
        result = number_1 % number_2
        print(result)
    elif operation == '**':
        result = number_1**number_2
        print(result)
    else:
        print("Error")
    calculator()

if __name__ == '__main__':
    calculator()
