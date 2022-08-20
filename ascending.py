
list = []

for c, i in enumerate(range(5)):
    num = int(input(f"{c+1} ->>> "))
    list.append(num)

for x in range(5):
    print(f"LOOP FIRST [{x}]")

    for o in range(5):

        print(f"LOOP SECOND [{x}][{o}]")

        if list[x] < list[o]:

            print(list, "EDIT")
            Temp = list[x]
            list[x] = list[o]
            list[o] = Temp
            print(list)
        else:
            print("%%%%%%%%%%%%%%%%%%%%")

for i in range(5):

    print(list[i])

'''
the list[x] moves to the end of a list as the
index increases, if the current main loop's 
index is 2 then the greatest at the moment will
be in index 2 of it's own list. & as this process
repeats eventually our list will come in a order.
so making a condition for list[o] to be greater 
means the list will be in ascending order bcuz
having greater value list [o] means greater 
value for list[x] as the approval of conditon 
swaps the values.
so bigger value for the second loop in condition
directly means that in the output the results
will be printed in ascending order......

the mechanics is similar to puzzle game
'''
