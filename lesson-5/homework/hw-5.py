#task1

year = int(input('Enter a year to check if it is a leap year: '))

if(year % 4 == 0):
    if(year % 400 == 0):
        print(f"{year} is a leap year")
    elif(year % 100 == 0):
        print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#task2

#    If n is odd, print Weird
 #   If n is even and in the inclusive range of 2 to 5, print Not Weird
  #  If n is even and in the inclusive range of 6 to 20, print Weird
   # If n is even and greater than 20, print Not Weird

n = int(input("Enter an integer: \n"))

if(n < 0 or n > 100):
    print(f'{n} n must be within 1 and 100 inclusively')
else:
    if(n % 2):
        print('Weird')
    else:
        if(n < 5):
            print('Not Weird')
        elif(n < 21):
            print('Weird')
        else:
            print('Not Weird')


#task3

#solution1
a = int(input('Number a:'))

b = int(input('Number b:'))

if(a % 2):
    if(b % 2):
        print('None are even')
    else:
        print('b is even')
else:
    if(b % 2):
        print('a is even')
    else:
        print('Both are even')

#solution2

if(a % 2 == 0 and b % 2 == 0):
    print('a and b are even')
elif(a % 2 and b % 2):
    print('None are even')
elif(a % 2):
    print('b is even')
else:
    print('a is even')

