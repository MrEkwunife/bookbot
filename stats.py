"""
get_str_words - calculates and returns the number of words found in a string
@str: input string
Returns: num words in @str
"""


def get_num_words(str):
    return len(str.split())


"""
get_char_counts - counts the number of char in the text converting
characters to lowercase ones
@text: input of which the individaul chars will be counted
Return: a dictionary mapping the chars with it's count {'p': 6121, 'r': 20818, 'o': 25225, ...}
"""


def get_char_counts(text):
    counts = {}

    for char in text:
        c = char.lower()
        counts[c] = counts.get(c, 0) + 1

    return counts
