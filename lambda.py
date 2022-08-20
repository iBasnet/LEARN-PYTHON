

# # print the sqaure of a number
# square = lambda n:n**2


# print(square(2))


# # greater among two numbers
# greater = lambda a,b: a if a > b else b


# print(greater(69, 33))


# sorting names by their length

names = ["Pratik", "Sam", "CZ", "Tim", "Messi", "Ronaldo"]

names.sort(key=lambda x: len(x))

print(names)

# shortest method
names = ["Pratik", "Sam", "CZ", "Tim", "Messi", "Ronaldo"]

names.sort(key=len)
print(names)

# example

list = [1, 2, 3, 4, 5, 6, 7]

squared = []


def square(n): return n**2


for n in list:
    squared.append(square(n))

print(squared)
