

def main():

    try:
        num1 = int(input("ENTER DIVIDENT ->>> "))
        num2 = int(input("ENTER DIVISOR ->>> "))
        num3 = num1/num2
        num4 = num1 % num2
        print(f"THE QUOTIENT IS {num3:.3f}")
        if num4 > 0:
            print(f"THE REMAINDER IS {num4}.")

    except ZeroDivisionError:
        print("DIVISOR MUST BE GREATER THAN ZERO!")

    except ValueError:
        print("PLEASE, ENTER VALID NUMBERS!")

    finally:
        ask = input("Type 'R' To Play Again! ->>> ").upper()
        if ask == 'R':
            main()


main()
