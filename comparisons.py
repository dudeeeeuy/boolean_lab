# Run the tests, then change the functions and test expectations
# The tests need to pass and the function needs to meet the requirements

def greater_than_one():
    # this function should return True if the input is greater than 1 (should work for floats and int)
    input_number = input("Pick a number, any number! ")
    return float(input_number) > 1


def you_are_number_one_alphabetically():
    # this function should return true if your name is alphabetically first
    # Hint: you can use the .upper() or .lower() functions on a string to return all lowercase or uppercase
    your_alien_classmate = "Zzanqfdort"
    your_name = input("What's your name? ")
    return your_name.lower() < your_alien_classmate.lower()


def are_you_voting_age():
    # this function should return true if you are 18 or older
    your_age = input("What's your age? ")
    return int(your_age) >= 18


def were_not_so_different_you_and_i():
    # this function should return true if the two inputs are the same
    input_1 = input("Enter a value: ")
    input_2 = input("Enter another value: ")
    return input_1 == input_2


def we_are_not_the_same():
    # this function should return true if the input is different than the variable
    pi = 3.14159
    input_pi = input("Do you like pi? ")
    return input_pi != pi