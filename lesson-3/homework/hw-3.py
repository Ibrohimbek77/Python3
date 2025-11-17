#task1

fruits = ['Apple', 'Orange', 'Banana', 'Strawberry', 'Lemon']

print(fruits[2])

#task2

nums1 = [1, 2, 3, 4, 5]

nums2 = [6, 7, 8, 9, 10]

nums1 += nums2

print(nums1)


#task3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

nums = [numbers[0], numbers[len(numbers) // 2], numbers[-1]]

print(nums)

#task4

movies = ['Edge Of Future', 'Transformesr: Dark Moon', 'Blame', 'Spy X Family']

movies = tuple(movies)

#task5

cities = ('England', 'Alfonso State', 'Kazimierz', 'Kazdel', 'Paris', 'Victoria', 'Ursus', 'Yan', 'Iberia', 'Lungmen')

if 'Paris' in cities:
   print(f"Paris is in the list under index {cities.index('Paris')}")

#task6

numerics1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numerics2 = numerics1.copy()

print(numerics1, numerics2)

#yask7

Numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"task 7 first and 2nd: \n{Numlist}")

temp = Numlist[0]

Numlist[0], Numlist[-1] = Numlist[-1], Numlist[0]

print(Numlist)

#task8

numtuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f" task 8 from 3 to 7 {numtuple[2:7]}")

#task9

colors = ["red", "blue", "green", "blue", "yellow", "blue", "orange"]

print(f"number of blue colors in {colors} is {colors.count('blue')}")

#task10

animals = ("cat", "dog", "elephant", "lion", "tiger")

print(f"task10 {animals} index of 'lion' {animals.index('lion')}")


#task11

tuplenum1 = (1, 2, 3)

tuplenum2 = (4, 5, 6)

newltuplenum = tuplenum1 + tuplenum2

print(newltuplenum, "task11")

#task12

my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30)

list_length = len(my_list)
tuple_length = len(my_tuple)

print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)

#task13

tupleSubesu = (1, 2, 4, 'Cibo', 'Killy')

print(tupleSubesu)

listSubesu = list(tupleSubesu)

listSubesu.append('SanakanWhyyy')

print(listSubesu)

#task14

tupleNumsiliconLife = (4, 2, 6, 3, 34, 7, 3, 1, 346, 6)

minSiliconLife = min(tupleNumsiliconLife)

maxSiliconLife = max(tupleNumsiliconLife)

print("min and max silicon life ", minSiliconLife, maxSiliconLife )

#task15

tupleWordsAdministration = ('You', 'kill', "Will", 'I')

print(tupleWordsAdministration, "   ", tupleWordsAdministration[::-1])

