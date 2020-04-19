

def is_unique(str):
    """ This function determine if a string contains all unique characters."""

    # Check the string length, it can not be more than 128 characters
    if len(str) > 128:
        return False

    # Initialize occurrence of all chars to False
    chars = [False] * 128

    # For every character, check if it exists in chars
    for i in range(0, len(str)):

        # Find ASCII value and check if it exists in set.
        value = ord(str[i])
        if chars[value]:
            return False
        chars[value] = True
    return True


str = "abbcd"
print(is_unique(str))
