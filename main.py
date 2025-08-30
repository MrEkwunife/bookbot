import sys
from stats import get_word_count, char_count_dict, sorted_list_dict

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    count_dict = char_count_dict(book_text)
    list_dict = sorted_list_dict(count_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for di in list_dict:
        if not di['char'].isalpha():
            continue

        print(f"{di['char']}: {di['num']}")

    print("============= END ===============")

main()
