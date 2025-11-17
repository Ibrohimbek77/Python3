import math
#task1

SquareSide = float(input('Enter the side of a square: '))

P = 4 * SquareSide

S = SquareSide ** 2

print("Perimeter : " + str(P))

print("Area : " + str(S))


#task2

diameterCircle = float(input('Enter diameter of a circle: '))

Circle = diameterCircle * 3.14

print("Circle : " + str(Circle))


#task3

a = float(input('a: '))

b = float(input('b: '))

mean = (a + b) / 2.0

print("Mean : " + str(mean))


#task4

a1 = float(input('a: '))

b1 = float(input('b: '))

AplusB = a1 + b1

AmultiplyB = a1 * b1

sqa = a1 ** 2

sqb = b1 ** 2

print('a + b = ' + str(AplusB))

print('a * b = ' + str(AmultiplyB))

print('a^2 = ' + str(sqa))

print('b^2 = ' + str(sqb))
