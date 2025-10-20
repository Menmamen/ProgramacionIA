# Python exercises for AI Programming Course: Ejercicios de Estructuras Alternativas
# Exercises solved by Carmen Montalvo Luque, 10/2025

# 1. Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))

if age1 < age2:
    print("The first person is younger.")
elif age2 < age1:
    print("The second person is younger.")
else:
    print("Both are the same age.")

#--------------------------------------------------------------------------------------

# 2. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triángulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.
A = float(input("Enter side A: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))

# Check for right triangle using Pythagoras theorem
if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    print("It is a right triangle.")
elif A == B == C:
    print("It is an equilateral triangle.")
elif A == B or A == C or B == C:
    print("It is an isosceles triangle.")
else:
    print("It is a scalene triangle.")

#--------------------------------------------------------------------------------------

# 3. Escribir un programa que lea un año indicar si es bisiesto (un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")

#--------------------------------------------------------------------------------------

# 4. Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.
amount = int(input("Enter an amount in euros: "))

bills = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for b in bills:
    count = amount // b
    amount = amount % b
    if count > 0:
        print(count, "x", b, "€")

#--------------------------------------------------------------------------------------

# 5. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
day_number = int(input("Enter a number (1 to 7): "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Error: number must be between 1 and 7.")

#--------------------------------------------------------------------------------------

# 6. Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

largest = a  # start assuming 'a' is the largest

if b > largest:
    largest = b
if c > largest:
    largest = c

print("The largest number is:", largest)

#--------------------------------------------------------------------------------------

# 7. Realiza un programa que pida cinco números enteros y diga cuál es el mayor No se puede usar la función max().
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))

largest = n1

if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3
if n4 > largest:
    largest = n4
if n5 > largest:
    largest = n5

print("The largest number is:", largest)

#--------------------------------------------------------------------------------------

# 8. Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las siguientes:
# «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).
grade = float(input("Enter your exam grade (0 to 10): "))

if grade < 5:
    print("Suspenso")
elif grade < 7:
    print("Aprobado")
elif grade < 9:
    print("Notable")
elif grade < 10:
    print("Sobresaliente")
elif grade == 10:
    print("Matrícula de Honor")
else:
    print("Invalid grade.")