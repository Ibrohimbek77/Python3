#alright guys I've redone the 1st task with Chat-GPT because task1 description is too ambigious and example output does not make any freaking sense, there is no logic behind it




def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    char_count = 0  # count every character

    i = 0
    while i < len(txt):
        ch = txt[i]
        result.append(ch)
        char_count += 1

        # time to place underscore?
        if char_count == 3:
            place = i + 1  # try to place underscore after current char

            # shift forward while:
            # 1) the character is a vowel
            # 2) or the NEXT character already has an underscore
            while True:
                # cannot place at the very end
                if place >= len(txt):
                    break

                # check vowel at placement point
                if txt[place] in vowels:
                    place += 1
                    continue

                # check if already underscore after placement
                if place < len(txt) and txt[place] == '_':
                    place += 1
                    continue

                break

            # insert underscore if valid
            if place < len(txt):
                result.append("_")

            char_count = 0  # restart counting

        i += 1

    # remove trailing underscore if it was added
    if result and result[-1] == "_":
        result.pop()

    return "".join(result)

print(f'task1: {insert_underscores('hello')}')


#task2

n = int(input('input an interger n:'))

print('task2')

for i in range(0 , n):
    if(n < 1 or n > 20):
        print('n must be within 1 and 20')
        break
    print(i * i)


#task3
#ex-1

i = 1
print('task3 ex-1')

while(i < 11):
    print(i)
    i += 1

#ex-2

numstring = str()

n = int(input('Enter an integer n: '))

print('task3 ex-2')

for i in range(1 , n + 1):
    numstring += f'{i} '
    print(numstring)
    
#ex-3

n = int(input('Enter an integer n: '))
sum = 0


for i in range(1, n + 1):
    sum += i

print(f'task3 ex-3 {sum}')


#ex-4

n = int(input('Enter an integer n: '))
print('task3 ex-4')

for i in range(1, 11):
    print(n * i)

#ex-5

print('task3 ex-5')

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    print(i)

#ex-6

print('Task3 ex-6')

n = int(input('Enter an integer n: '))
numberOfdigits = 0

while(n > 0):
    numberOfdigits += 1
    n //= 10

print(numberOfdigits)

#ex-7

print('task3 ex-7')

numstring = str()

n = int(input('Enter an integer n: '))

i = n
j = i

while(i > 0):
    j = i
    while(j > 0):
        numstring += f'{j} '
        j -= 1
    print(numstring)
    numstring = ''
    i -= 1

#ex-8
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i])

#ex-9
for i in range(-10, 0):
    print(i)


#ex-10
for i in range(5):
    print(i)
else:
    print("Done!")

#ex-11
start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

#ex-12
n = 10
a, b = 0, 1

print("Fibonacci sequence:")

for _ in range(n):
    print(a, end="  ")
    a, b = b, a + b

#ex-13
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print(f"{n}! = {fact}")

#task4
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

uncommon = []

# elements in list1 but not in list2
for x in list1:
    if x not in list2:
        uncommon.append(x)

# elements in list2 but not in list1
for x in list2:
    if x not in list1:
        uncommon.append(x)

print(uncommon)
