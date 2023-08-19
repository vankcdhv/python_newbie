def readDataFromConsole():
    # Prompt the user for an integer input
    try:
        user_integer = int(input("Enter an integer: "))
        print("You entered:", user_integer)
        return user_integer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None


def readUserAge():
    try:
        user_age = int(input("Enter age of user: "))
        return user_age
    except ValueError:
        print("User age must be an integer")
