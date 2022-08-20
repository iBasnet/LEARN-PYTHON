

# programs that returns whether a number is odd or even

try:
    num = int(input("ENTER A NUMBER ->>> "))
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

except Exception:
    print("PLEASE ENTER A VALID NUMBER!")
