# Python exercises for AI Programming Course: Ejercicios de Funciones
# Exercises solved by Carmen Montalvo Luque, 10/2025


# Ejercicio 1
# Program with a menu to perform operations on two numbers

# --- Math operation functions ---
def add(a, b):
    print("Result:", a + b)

def subtract(a, b):
    print("Result:", a - b)

def multiply(a, b):
    print("Result:", a * b)

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:", a / b)

# --- Menu function ---
def show_menu(options):
    """Displays a numbered menu and returns user's choice"""
    print("\nMENU:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = input("Choose an option number: ")
    if choice.isdigit():
        return int(choice)
    else:
        return -1

# --- Exercise 1 main function ---
def run_exercise_1():
    a = 0
    b = 0
    numbers_set = False  # Control flag
    options = [
        "Enter values (a and b)",
        "Add",
        "Subtract",
        "Multiply",
        "Divide",
        "Exit"
    ]

    while True:
        choice = show_menu(options)

        if choice == 1:
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            numbers_set = True

        elif choice in [2, 3, 4, 5]:
            if not numbers_set:
                print("Error: Please enter values first (option 1).")
                continue
            if choice == 2:
                add(a, b)
            elif choice == 3:
                subtract(a, b)
            elif choice == 4:
                multiply(a, b)
            elif choice == 5:
                divide(a, b)

        elif choice == 6:
            print("Program ended.")
            break

        else:
            print("Invalid option, please try again.")



# Ejercicio 2
# Numeric functions library

def digits(n):
    """Returns the number of digits in n"""
    n = abs(n)
    count = 1
    while n >= 10:
        n //= 10
        count += 1
    return count

def reverse(n):
    """Reverses the digits of n"""
    neg = n < 0
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return -rev if neg else rev

def is_palindromic(n):
    """Returns True if n is palindromic"""
    return n == reverse(n)

def is_prime(n):
    """Returns True if n is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    """Returns the next prime greater than n"""
    n += 1
    while not is_prime(n):
        n += 1
    return n

def digit_n(n, pos):
    """Returns the digit at position pos (left to right, starting at 0)"""
    total_digits = digits(n)
    n = abs(n)
    for _ in range(total_digits - pos - 1):
        n //= 10
    return n % 10

def digit_position(n, d):
    """Returns the first position of digit d, or -1 if not found"""
    total_digits = digits(n)
    for i in range(total_digits):
        if digit_n(n, i) == d:
            return i
    return -1

def remove_behind(n, q):
    """Removes q digits from the right"""
    return n // (10 ** q)

def remove_ahead(n, q):
    """Removes q digits from the left"""
    return n % (10 ** (digits(n) - q))

def paste_behind(n, d):
    """Adds a digit behind"""
    return n * 10 + d

def paste_ahead(n, d):
    """Adds a digit ahead"""
    return d * (10 ** digits(n)) + n

def piece_of_number(n, start, end):
    """Returns the piece of n from start to end (inclusive)"""
    cut = remove_behind(n, digits(n) - end - 1)
    return remove_ahead(cut, start)

def concatenate(a, b):
    """Concatenates two numbers"""
    return a * (10 ** digits(b)) + b


# --- Testing all functions ---
def test_functions():
    print("\nTesting numeric functions:\n")
    print("Digits in 12345:", digits(12345))
    print("Reverse 1234:", reverse(1234))
    print("Is 1221 palindromic?", is_palindromic(1221))
    print("Is 13 prime?", is_prime(13))
    print("Next prime after 14:", next_prime(14))
    print("Digit 2 of 98765:", digit_n(98765, 2))
    print("Position of digit 8 in 98765:", digit_position(98765, 8))
    print("Remove 2 digits behind 12345:", remove_behind(12345, 2))
    print("Remove 2 digits ahead 12345:", remove_ahead(12345, 2))
    print("Paste digit 9 behind 123:", paste_behind(123, 9))
    print("Paste digit 9 ahead 123:", paste_ahead(123, 9))
    print("Piece of number 987654 from 1 to 3:", piece_of_number(987654, 1, 3))
    print("Concatenate 12 and 34:", concatenate(12, 34))
    print("\nAll functions tested successfully.\n")

def run_exercise_2():
    test_functions()



# Main program menu

def main_menu():
    options = [
        "Run Exercise 1 (calculator menu)",
        "Run Exercise 2 (numeric functions)",
        "Exit"
    ]

    while True:
        choice = show_menu(options)
        if choice == 1:
            run_exercise_1()
        elif choice == 2:
            run_exercise_2()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


# === PROGRAM START ===

if __name__ == "__main__":
    main_menu()
