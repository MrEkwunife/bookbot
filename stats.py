def get_word_count(texts):
    return len(texts.split())


def char_count_dict(texts):
    char_count = {}

    for text in texts:
        char_count[text.lower()] = char_count.get(text.lower(), 0) + 1

    return char_count


def sorted_list_dict(char_dict):
    list_dict = []

    def sort_on(item):
        return item["num"]

    for char, num in char_dict.items():
        list_dict.append({"char": char, "num": num})

    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
