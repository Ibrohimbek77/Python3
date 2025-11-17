#task1

Dictionary = {'Hello' : 4, 'Madame': 2, 'Default': 5}

DicSortedAsc = dict(sorted(Dictionary.items(), key = lambda givenPair: givenPair[1]))

DicSortedDesc = dict(sorted(Dictionary.items(), key = lambda givenPair: givenPair[1], reverse=True))

print(f'Task1 :Sorted ASC: {DicSortedAsc}\nSorted DESC {DicSortedDesc}\n')

#task2

Dictionary2 = {0: 10, 1: 20}

print(f'Task2: Initially {Dictionary2}')

Dictionary2.update(
    {2: 30}
)

print(f"After that {Dictionary2}\n")

#task3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print('Task3:')
print(f"Dic1 {dic1}")
print(f"Dic2 {dic2}")
print(f"Dic3 {dic3}")

finalDict = dict()

finalDict.update(dic1)
finalDict.update(dic2)
finalDict.update(dic3)

print(f"Finally total: {finalDict}\n")

#task4

x = int(input('Enter x: '))

resultdict = dict()

for i in range(1, x + 1):
    resultdict.update(
        {i : i * i}
    )

print(f"Task4 {resultdict}\n")

#task5

resultdict = dict()

for i in range(1, 16):
    resultdict.update(
        {i : i * i}
    )

print(f"Task5 {resultdict}\n")




#sets

#task6

newSet = set()

print("Task6 ", type(newSet), '\n')

#task7

newSet.update(finalDict)

print("Task7")

for i in newSet:
    print(i)


#task8

newSet.add(7)
newSet.add(8)

print("\n Task8 ")

print(newSet, "\n")

#task9

newSet.remove(1)

print("Task9 ", newSet, "\n")

#task10

x = int(input("Enter a number to check if in the set and remove it: "))

print("TASK 10: Item in the set removed" * int(x in newSet))

print("TASK 10: Item not in the set " * int(x not in newSet))

x in newSet and newSet.remove(x)

print(newSet)
