

# squaring numbers using map()
numbers = [1, 2, 3, 4, 5, 6, 7]

square_numbers = map(lambda n: n**2, numbers)

print(list(square_numbers))

# adding corresponding values of two list

values1 = [1, 2, 3]
values2 = [7, 8, 9]

sum = map(lambda n1, n2: n1+n2, values1, values2)

print(list(sum))

# filter()

even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print(even_numbers)
