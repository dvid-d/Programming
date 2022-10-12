import operator

operators = {"+":operator.add, "-".operator.sub, "*":operator.mul, "/":operator.truediv}

def table():
    operator_user = str(input("Enter an operator"))
    n = str(input("Enter a natural number"))
    try:
        if not operator_user in operators:
            raise NameError()
        if operator_user == "/" and n == 0:
            raise ZeroDivisionError()
    ##
    else:
        line_one = []
        for i in range(0, n+1):
            line_one.append(i)
        print(f"{operator_user} | ")
        for j in range(0, n):
            print(line_one[j], end = ' ')
        print("-"*(n*3))
        if operator_user == "+":
            for i in range(0,n+1):
                print(i, end = ' ')
                print("|", end = ' ')
                if i == 0:
                    for i in range(0, n+1):
                        print(i, end = ' ')
                else:
                    print(i+1,end=' ')
                print(" ")
