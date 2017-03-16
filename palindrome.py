# coding: utf-8

def is_palindrome(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('apple')
    False
    """

    # Initialize position variables.
    i = 0
    j = len(s) - 1

    # Continue through positions until middle is reached.
    while i < j and s[i] == s[j]:
        # Move closer to middle
        i += 1
        j -= 1

    # If we reached the middle, return True.
    # Else return False.
    return j <= i

if __name__ == '__main__':
    word = input('Enter a word: ')
    if is_palindrome(word):
        print(word, 'is a palindrome.')
    else:
        print(word, 'is not a palindrome.')
