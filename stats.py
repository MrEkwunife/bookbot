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


"""
get_sorted_chars_data - takes a dictionary of chars and their counts (i.e {'a': 34, 'c': 456, ...}) and
makes a list of dictionary out of them with each character having it own object like:
    {"name": "a", "num": 34}, {"name": "b", "num": 456}. The list will be sorted in decending
order.
@char_dict:
    dictionary of characters with their counts
Return:
    list of dictionary having keys "char" (for the character) and "num" to specify their count,
    sorted in decending order based on the num
"""


def get_sorted_chars_data(char_dict):
    chars_data_lst = []

    def sort_on(items):
        return items["num"]

    for key, value in char_dict.items():
        d = {"name": key, "num": value}
        chars_data_lst.append(d)

    chars_data_lst.sort(reverse=True, key=sort_on)
    return chars_data_lst
