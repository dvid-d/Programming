import operator

operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}

def table():
    operator_user = str(input("Enter an operator: ")) #asks user for operator
    n = int(input("Enter a natural number: ")) #asks user for a number
    a = 0
    while a < (n+1):
        if a == 0:
             print(f"{a}  | ", end = ' ')
             a += 1
        else:
            print(f"{a}  ", end = ' ')
            a += 1
    print("\n" + "----"*(n+1))
    for i in range(0, n):
        if i == 0:
            print(f"{i}  | ", end = ' ')
        else:
            print(operators[operator_user](i, 1), end == ' ')
