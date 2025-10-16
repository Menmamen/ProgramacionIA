# Python exercises for AI Programming Course: Ejercicios de Estructuras Secuenciales
# Exercises solved by Carmen Montalvo Luque

# 1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
name = input("What is your name? ")
print(f"Hello, {name}!")

# 2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
cathetus1 = float(input("Enter the length of the first cathetus: "))
cathetus2 = float(input("Enter the length of the second cathetus: "))
hypotenuse = math.sqrt(cathetus1**2 + cathetus2**2)
print(f"The hypotenuse is: {hypotenuse}")

# 3. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
total_minutes = int(input("Enter the number of minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutes are {hours} hours and {minutes} minutes.")

# 4. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.
number = int(input("Enter a two-digit number: "))
tens = number // 10
units = number % 10
reversed_number = units * 10 + tens
print(f"The inverted number is: {reversed_number}")

# 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un programa que determine la hora de llegada a la ciudad B.
hours = int(input("Enter the starting hour (HH): "))
minutes = int(input("Enter the starting minutes (MM): "))
seconds = int(input("Enter the starting seconds (SS): "))
travel_time = int(input("Enter the travel time in seconds: "))

# Convert start time to total seconds, add travel time, and convert back
total_seconds = hours * 3600 + minutes * 60 + seconds + travel_time
arrival_hour = (total_seconds // 3600) % 24
arrival_minute = (total_seconds % 3600) // 60
arrival_second = total_seconds % 60

print(f"Arrival time is {arrival_hour:02d}:{arrival_minute:02d}:{arrival_second:02d}")

# 6. Escribir un programa para calcular la nota final de un examen, considerando que:
#     Cada respuesta correcta suma 5 puntos.
#     Cada respuesta incorrecta suma -1 puntos.
#     Cada respuesta en blanco suma 0 puntos.
#     Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

correct = int(input("Enter number of correct answers: "))
incorrect = int(input("Enter number of incorrect answers: "))
blank = int(input("Enter number of blank answers: "))

# Define point values in variables to make future changes easy
points_correct = 5
points_incorrect = -1
points_blank = 0

# Compute score
total_score = (correct * points_correct) + (incorrect * points_incorrect) + (blank * points_blank)

# Normalize to a 0–10 scale (assuming maximum possible is all correct)
max_score = (correct + incorrect + blank) * points_correct
if max_score == 0:
    normalized_score = 0
else:
    normalized_score = (total_score / max_score) * 10

print(f"Total score: {total_score}")
print(f"Normalized score (0–10): {normalized_score:.2f}")

# → Para facilitar que los puntos puedan cambiar en el futuro:
# Use variables (like 'points_correct', 'points_incorrect', etc.) or store them in a dictionary.
# That way, you only need to modify one place in the code if the scoring system changes.
