def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_analysis(count_words(file_contents), char_dict(file_contents))


def count_words(strs):
    return(len(strs.split()))


def char_dict(strs):
    char_obj = {}
    words = strs.lower()

    for word in words:
        char_obj[word] = char_obj.get(word, 0) + 1
    
    return (dict(sorted(char_obj.items(), key=lambda item: item[1], reverse=True)))


def print_analysis(word_c, char_d):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_c} words found in the document\n")

    for char, cnt in char_d.items():
        if char.isalpha():
            print(f"The '{char}' character was found {cnt} times")

    print("--- End report ---")


main()