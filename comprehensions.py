import math


# printing first 10 natural numbers
numbers1 = [x for x in range(1, 11)]
print("->>>", numbers1)


# printing even numbers upto 20
numbers2 = [x for x in range(1, 21) if x % 2 == 0]
print("->>>", numbers2)


# printing odd numbers upto 20
numbers2 = [x for x in range(1, 21) if x % 2 != 0]
print("->>>", numbers2)


# printing multiples of 5 upto 50
numbers3 = [x for x in range(1, 51) if x % 5 == 0]
print("->>>", numbers3)


# printing the square root of numbers
numbersz = [1, 4, 9, 16, 25, 36, 49]
numbers4 = [math.sqrt(num) for num in numbersz]
print("->>>", numbers4)


# printing nested list
place = ["Las Vegas", "Sydney"]
vehicle = ["Car", "Bike"]
luck = [(x, y) for x in place for y in vehicle]
print("->>>", luck)


# square of numbers in dict using for loop
numbers = [1, 2, 3, 4, 5, 6, 7]

dict = dict()

for num in numbers:
    dict[num] = num**2

print("->>>", dict)


# square of numbers in dict using for loop

dictt = {num: num**2 for num in numbers}
print("->>>", dictt)


# eample with dict
price = {"iphone": 999, "pc": 1799, "console": 399}

newprice = {key: value-300 if value >
            700 else value for (key, value) in price.items()}
print(newprice)
