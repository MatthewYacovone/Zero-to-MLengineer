
# Function to check whether a number is prime or not

import math
def is_prime(n):
    """
    Determines if a number is prime.
    Returns True if prime, False otherwise.
    """
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    # Loop from 5 to √n, incrementing by 6.
    # Checks if n is divisible by i (which corresponds to 6k+1) or by i+2 (which corresponds to 6k+5).
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6 # check 11 and 13, and so on...

    return True

def user_interaction():
    """
    Handles user input and interaction in a loop.
    """
    while True:
        try:
            n = int(input("Enter a number and see if it's prime: "))
            if is_prime(n):
                print(f"{n} is a prime number.\n")
            else:
                print(f"{n} is not a prime number.\n")
        except ValueError:
            print("Please enter an integer. \n")

        stop = input("Would you like to try again? Enter y or n. ").lower()

        if stop == "n":
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    user_interaction()

