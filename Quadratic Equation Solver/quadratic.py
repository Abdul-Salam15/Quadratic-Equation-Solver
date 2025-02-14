import math

#Coefficients of the quadratic equation
a = float(input('Enter the coefficient of a: '))
b = float(input('Enter the coefficient of b: '))
c = float(input('Enter the coefficient of c: '))

#Calculate the first part b**2 - 4*a*c (lets call it first_part)
first_part = b**2 - 4*a*c

#Check if its either positie, negative or zero
if first_part > 0 :
    root1 = (-b + math.sqrt(first_part)) / (2*a)
    root2 = (-b - math.sqrt(first_part)) / (2*a)

    print(f'X: {root1}')
    print(f'Y: {root2}')

elif first_part == 0 :
    root = -b / (2*a)
    print(f'Root: {root}')

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(first_part)) / (2*a)
    print(f'X: {real_part} + {imaginary_part} i')
    print(f'Y: {real_part} - {imaginary_part} i')

quit()