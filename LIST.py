

a = [2, 5, 4, 3, 1]

# beginner

ascending = sorted(a)

print(ascending)


# intermediate

a = [2, 5, 4, 3, 1]

b = []


for o in range(5):

    x = min(a)
    b.append(x)
    a.remove(x)

print(b)


# advanced


a = [2, 5, 4, 3, 1]

b = []

for i in range(5):

    for num in a:

        x = map(lambda x: x >= num, a)

        if False in x:
            pass

        else:
            b.append(num)
            a.remove(num)


print(b)

# expert

a = [2, 5, 4, 3, 1]

b = []

while a:
    s = a[0]
    for x in a:
        if x < s:
            s = x
    b.append(s)
    a.remove(s)

print(b)

# master

list = []

for c, i in enumerate(range(5)):
    num = int(input(f"{c+1} ->>> "))
    list.append(num)

for x in range(5):

    for o in range(5):

        if list[x] < list[o]:

            Temp = list[x]
            list[x] = list[o]
            list[o] = Temp

for i in range(5):

    print(list[i])
