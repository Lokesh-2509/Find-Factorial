def factorial_recursive(A):
    if A == 0:
        return 1
    else:
        return A * factorial_recursive(A - 1)
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer to find its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial_recursive(num)
            print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
