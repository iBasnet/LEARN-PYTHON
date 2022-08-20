

# list of natural numbers
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# printing first 5 elements of list
print(list[:5])

# printing last 5 elements of list
print(list[-5:])

# printing list in reverse order
print(list[::-1])

# printing list in reverse + step 2
print(list[::-1][::2])

# normalizing the order + step 2
print(list[::-1][::2][::-1])

# printing odd numbers from the list
print(list[::2])

# printing even numbers from the list
print(list[1::2])


# normal string
name = "Pratik Basnet 2006"

# changing the string into list
x = name.split()
print(x)

# printing the first word of the list
print(x[0])

# printing the first letter of the first word
print(x[0][0])

# printing the second word of the list
print(x[0])

# printing the first letter of the second word
print(x[1][0])

# changing the first word of the list
x[0] = "Lord"
print(x)

# changing the second word of the list
x[1] = "Ansh"
print(x)

# changing the third element of the list
x[2] = "2004"
print(x)
