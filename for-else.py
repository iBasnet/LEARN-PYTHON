

# check availability of a element
from __future__ import print_function


languages = ["QBasic", "C", "Python", "HTML", "CSS", "Javascript", "Solidity"]

for language in languages:
    if language == "Solidity":
        print("Found!")
        break
else:
    print("NOT Found!")


#prime or composite

def main():

    try:
        str = input("ENTER A NUMBER ->>> ")
        num = int(str)
        i = 2
        while i < num:
            if num % i == 0:
                print(f"{num} is a Composite number.\nIt's {num//i} times {i}.")
                break
            i += 1
        else:
            print(f"{num} is a Prime number.")

    except ValueError:
        print(f'"{str}" IS NOT A INTEGER!')
        main()


main()
