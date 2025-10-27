# Python exercises for AI Programming Course: Ejercicios de Estructuras Repetitivas
# Exercises solved by Carmen Montalvo Luque, 10/2025

# 1. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
print("\n--- 1. Even numbers between two numbers ---")

start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

print("Even numbers between", start, "and", end, ":")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)

#--------------------------------------------------------------------------------------

# 2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
print("\n--- 2. Count positive, negative, and zero numbers ---")

count = int(input("How many numbers will you enter? "))

greater = 0
less = 0
equal = 0

for i in range(count):
    num = float(input("Enter a number: "))
    if num > 0:
        greater += 1
    elif num < 0:
        less += 1
    else:
        equal += 1
print("Numbers greater than 0:", greater)
print("Numbers less than 0:", less)
print("Numbers equal to 0:", equal)

#--------------------------------------------------------------------------------------

# 3. Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.
print("\n--- 3. Guess the number (1 to 100) ---")

import random
secret = random.randint(1, 100)
attempts = 10
found = False

while attempts > 0 and not found:
    guess = int(input("Enter your guess (1 to 100): "))
    attempts -= 1
    if guess == secret:
        print("You guessed it! The number was", secret)
        print("You used", 10 - attempts, "attempt(s).")
        found = True
    elif guess < secret:
        print("The number is greater. Attempts left:", attempts)
    else:
        print("The number is smaller. Attempts left:", attempts)

if not found:
    print("You ran out of attempts. The number was:", secret)

#--------------------------------------------------------------------------------------

# 4. Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.
print("\n--- 4. Numbers inside and outside an interval ---")

# Ask for interval limits
while True:
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))
    if lower < upper:
        break
    else:
        print("Error: lower limit must be smaller than upper limit.")

sum_inside = 0
count_outside = 0
equal_limit = False

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    if lower < n < upper:
        sum_inside += n
    else:
        count_outside += 1
    if n == lower or n == upper:
        equal_limit = True

print("Sum of numbers inside the interval:", sum_inside)
print("Numbers outside the interval:", count_outside)
if equal_limit:
    print("You entered a number equal to one of the limits.")
else:
    print("No number equal to the limits was entered.")

#--------------------------------------------------------------------------------------

# 5. Crea un programa que pida un número por teclado al usuario y diga si es primo. En caso de que no se introduzca un número o que esta sea menor que 2 se debe mostrar un mensaje de error.
print("\n--- 5. Check if a number is prime ---")

num = input("Enter a number greater than 1: ")

if not num.isdigit():
    print("Error: you must enter a positive integer.")
else:
    num = int(num)
    if num < 2:
        print("Error: number must be 2 or greater.")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")

#--------------------------------------------------------------------------------------

# 6. Crea un programa que muestre en pantalla los N primeros número primos. El valor de N se pide por teclado al usuario/a.
print("\n--- 6. Show the first N prime numbers ---")

N = int(input("How many prime numbers do you want to see? "))

count = 0
num = 2

while count < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1

#--------------------------------------------------------------------------------------

# 7. Crea un programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización después de que se pida al usuario/a:
# Importe del préstamo.
# La tasa de interés anual.
# Y el plazo de pago en años.
print("\n--- 7. Mortgage payment and amortization table ---")

# Ask for inputs
loan = float(input("Enter the loan amount: "))
annual_interest = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the payment term (in years): "))

# Basic calculations
monthly_interest = annual_interest / 100 / 12
months = years * 12

# Monthly payment formula
payment = loan * (monthly_interest * (1 + monthly_interest) ** months) / ((1 + monthly_interest) ** months - 1)

print("\nMonthly payment: {:.2f} €".format(payment))
print("\nAmortization table:")
print("Month\tPayment\t\tInterest\tPrincipal\tRemaining balance")

balance = loan

for m in range(1, months + 1):
    interest = balance * monthly_interest
    principal = payment - interest
    balance -= principal
    print("{}\t{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(m, payment, interest, principal, balance if balance > 0 else 0))
    