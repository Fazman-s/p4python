# Python3 program to mark numbers
# as multiple of 2 or 5
import math

# Function to mark multiples of 2 and 5
def markMultiples(a, b):
    size = abs(b - a) + 1
    array = [0] * size

    # Iterate through a to b,
    # If it is a multiple of 2
    # or 5, mark index in array as 1
    for i in range(a, b + 1):
        if (i % 2 == 0 or i % 5 == 0):
            array[i - a] = 1

    print("MULTIPLES of 2 and 5:")
    for i in range(a, b + 1):
        if (array[i - a] == 1):
            print(i, end=" ")

# Main function
def main():
    a, b = map(int, input().split())
    markMultiples(a, b)

if __name__ == "__main__":
    main()
