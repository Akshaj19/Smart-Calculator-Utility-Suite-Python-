# Smart Calculator & Utility Program in Python
# Make a experience 


def greatest_of_three():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print("Greatest Number =", max(a, b, c))

def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum =", a + b)

def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Subtraction =", a - b)

def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Multiplication =", a * b)

def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Division =", a / b)
    else:
        print("Division by zero is not allowed.")

def even_or_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

def swap_numbers():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    a, b = b, a
    print("After Swapping: First =", a, "Second =", b)

def simple_interest():
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate: "))
    t = float(input("Enter Time: "))
    si = (p * r * t) / 100
    print("Simple Interest =", si)

while True:
    print("\n==============================")
    print(" Smart Calculator & Utility ")
    print("==============================")
    print("1. Greatest of 3 Numbers")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. Division")
    print("6. Even or Odd")
    print("7. Swap Two Numbers")
    print("8. Simple Interest")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        greatest_of_three()
    elif choice == '2':
        addition()
    elif choice == '3':
        subtraction()
    elif choice == '4':
        multiplication()
    elif choice == '5':
        division()
    elif choice == '6':
        even_or_odd()
    elif choice == '7':
        swap_numbers()
    elif choice == '8':
        simple_interest()
    elif choice == '9':
        print("Exiting Program... Thank You!")
        break
    else:
        print("Invalid choice! Please try again.")
