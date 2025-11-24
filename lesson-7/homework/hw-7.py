import math


#task1

def is_prime(n) -> bool:
    if(n == 1):
        return True
    limit = math.sqrt(n)
    currentN = 2

    while (currentN <= limit):
        if(n % currentN == 0):
            return False
        currentN += 1
    return True
            
number = -1

while(number < 1):
    number = int(input('Enter a number n > 0: '))

print(f'task1: {is_prime(number)}')


#task2

def digit_sum(k) -> int:
    sum = 0
    while (k):
        sum += k % 10
        k //= 10
    return sum

k = int(input('Task2: Enter a number: '))

print(f'Sum of {k}\'s digits is {digit_sum(k)}')

#task3

numbers = str()

def degreesTillN(n) -> str:
    if(n < 1):
        return
    if(n == 1):
        print(1)
        return
    degree = 1
    numbers = str()
    while(2 ** degree <= n ):
        numbers += f'{2 ** degree} ' 
        degree += 1

    return numbers
    


k = int(input('Task3: Enter a number n > 0: '))

numbers = degreesTillN(k)

print(numbers)
