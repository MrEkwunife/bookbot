import sys

from stats import get_char_counts, get_num_words, get_sorted_chars_data

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
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        file_contents = get_book_text(sys.argv[1])
        num_words = get_num_words(file_contents)
        chars = get_char_counts(file_contents)
        sorted_char_lst = get_sorted_chars_data(chars)

        print("============ BOOKBOT ============")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for char_dict in sorted_char_lst:
            if char_dict["name"].isalpha():
                print(f"{char_dict['name']}: {char_dict['num']}")

        print("============= END ===============")
    except FileNotFoundError:
        print(f"{sys.argv[1]} is not in the books directory")
        sys.exit(1)


main()
