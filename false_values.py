# Run the tests, then change the functions and test expectations
# The tests need to pass and the function needs to meet the requirements

def false_boolean():
    # This function already returns a boolean value that is false
    return not True


def false_string():
    # This function should return a string value that will be converted to false by the bool() function
    return 'false'


def false_int():
    # This function should return an integer value that will be converted to false by the bool() function
    return -22


def false_float():
    # This function should return a float value that will be converted to false by the bool() function
    return -2.71