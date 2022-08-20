

def main(*args, **kwargs):

    print(args, kwargs)
    kwargs["name"], kwargs["surname"] = "Cozey", "Swift"
    print(args, kwargs)


main(1, 2, 3, name="Pratik", surname="Basnet")


# adder function using args
def adder(*num):
    sum = 0

    for n in num:
        sum += n
    print("The Sum is", sum)


adder(1, 2, 3, 4)
adder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# printer function using kwargs


def details(**data):

    print("DATA TYPE OF ARGUMENT: ", type(data))

    for key, value in data.items():
        print(f"{key} is {value}.")


details(Name="Pratik Basnet", Age="16", Work="Programmer")
details(Name="Cozey", Channel="@CozeyCodes", Company="Zizzel Inc")
