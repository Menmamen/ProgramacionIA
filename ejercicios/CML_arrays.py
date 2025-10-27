# Python exercises for AI Programming Course: Ejercicios de Funciones
# Exercises solved by Carmen Montalvo Luque, 10/2025

import random
import numpy as np

# Ejercicio 1

# Define three lists: number, square, and cube.
# Fill 'number' with random integers from 0 to 100.
# 'square' contains their squares, 'cube' their cubes.
# Display them in three columns.

def exercise_1():
    number = []
    square = []
    cube = []

    # Fill the list with random numbers and compute square and cube
    for i in range(20):
        n = random.randint(0, 100)
        number.append(n)
        square.append(n ** 2)
        cube.append(n ** 3)

    # Display results in columns
    print(f"{'Number':>10} {'Square':>10} {'Cube':>10}")
    print("-" * 32)
    for i in range(20):
        print(f"{number[i]:>10} {square[i]:>10} {cube[i]:>10}")



# Ejercicio 2
# Same as exercise 1 but using numpy for calculations.

def exercise_2():
    number = np.random.randint(0, 101, 20)
    square = number ** 2
    cube = number ** 3

    print(f"{'Number':>10} {'Square':>10} {'Cube':>10}")
    print("-" * 32)
    for n, s, c in zip(number, square, cube):
        print(f"{n:>10} {s:>10} {c:>10}")



# Ejercicio 3
# Generate 20 random integers (0–100) in a numpy array.
# Move even numbers to the beginning, odd numbers to the end.

def exercise_3():
    numbers = np.random.randint(0, 101, 20)
    print("Original array:\n", numbers)

    even = numbers[numbers % 2 == 0]
    odd = numbers[numbers % 2 != 0]
    result = np.concatenate((even, odd))

    print("\nReordered array (evens first):\n", result)


# Ejercicio 4
# Read 5 numbers from keyboard into a list and rotate them:
# last element moves to first position.

def exercise_4():
    numbers = []
    for i in range(5):
        n = int(input(f"Enter number {i+1}: "))
        numbers.append(n)

    print("\nOriginal list:", numbers)

    # Rotate elements
    last = numbers.pop()     # Remove last element
    numbers.insert(0, last)  # Insert it at the beginning

    print("Rotated list:", numbers)


# Ejercicio 5
# Generate 20 integers (100–999) into a 4x5 list (matrix).
# Show partial sums by rows and columns like a spreadsheet.

def exercise_5():
    rows = 4
    cols = 5

    # Create 4x5 matrix
    matrix = [[random.randint(100, 999) for _ in range(cols)] for _ in range(rows)]

    # Calculate sums
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]
    total_sum = sum(row_sums)

    # Display table with sums
    print("\nMatrix with row and column sums:\n")
    for i in range(rows):
        for j in range(cols):
            print(f"{matrix[i][j]:>6}", end=" ")
        print(f"| {row_sums[i]:>6}")
    print("-" * 45)

    for j in range(cols):
        print(f"{col_sums[j]:>6}", end=" ")
    print(f"| {total_sum:>6}")


# Ejercicio 6
# Same as exercise 5 but using numpy.

def exercise_6():
    matrix = np.random.randint(100, 1000, (4, 5))

    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    total_sum = np.sum(matrix)

    print("\nMatrix with row and column sums (using numpy):\n")
    for i in range(4):
        for j in range(5):
            print(f"{matrix[i, j]:>6}", end=" ")
        print(f"| {row_sums[i]:>6}")
    print("-" * 45)
    for val in col_sums:
        print(f"{val:>6}", end=" ")
    print(f"| {total_sum:>6}")


# Main menu

def show_menu(options):
    print("\nMENU:")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    choice = input("Choose an option number: ")
    if choice.isdigit():
        return int(choice)
    return -1


def main():
    options = [
        "Exercise 1 - Lists: number, square, cube",
        "Exercise 2 - Same with numpy",
        "Exercise 3 - Move even numbers first (numpy)",
        "Exercise 4 - Rotate list elements",
        "Exercise 5 - 4x5 table with sums",
        "Exercise 6 - Same with numpy",
        "Exit"
    ]

    while True:
        choice = show_menu(options)
        if choice == 1:
            exercise_1()
        elif choice == 2:
            exercise_2()
        elif choice == 3:
            exercise_3()
        elif choice == 4:
            exercise_4()
        elif choice == 5:
            exercise_5()
        elif choice == 6:
            exercise_6()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


# === PROGRAM START ===

if __name__ == "__main__":
    main()
