

def getFactorial(num):

    factorial = 1

    for i in range(1, num+1):

        factorial = factorial * i

    return factorial


try:
    num = int(input("ENTER A NUMBER ->>> "))

except ValueError:
    print("MUST INPUT INTEGERS!")
    exit()

print(getFactorial(num))
