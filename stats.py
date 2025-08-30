def get_word_count(texts):
    return len(texts.split())


def char_count_dict(texts):
    char_count = {}

    for text in texts:
        char_count[text.lower()] = char_count.get(text.lower(), 0) + 1

    return char_count
