from stats import get_char_counts, get_num_words

"""
get_book_text - returns contents of a file
@file_path - path to file whose contents is to be returned
Return: contents of file_path
"""


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


# Program entry point
def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(file_contents)
    chars = get_char_counts(file_contents)

    print(f"Found {num_words} total words")
    print(chars)


main()
