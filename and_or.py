# Run the tests, then change the functions and test expectations
# The tests need to pass and the function needs to meet the requirements

def between_zero_and_one(number):
    # function should return true if the function input "number" is between zero and one (but not zero or one)
    return 0 < number < 1



def integer_or_float(value):
    # function should return true if the function type is integer or float, false for other types
    return type(value) == int or type(value) == float