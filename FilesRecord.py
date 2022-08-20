

name = input("NAME YOUR FILE ->>> ")

with open(name, "w") as f:

    a = input("NAME ->>> ").title()
    b = str(input("AGE ->>> "))
    c = str(input("CLASS ->>> "))
    d = input("ADDRESS ->>> ").title()

    dict = {
        'name': a,
        'age': b,
        'class': c,
        'address': d
    }

    f.write(str(dict))
