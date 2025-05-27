def get_num_words(book):
    words = book.split()
    return len(words)

def character_nums(book):
    book_characters = list(book.lower())
    characters = {}
    for i in range(len(book_characters)):
        c = book_characters[i]
        if (c in characters):
            characters[book_characters[i]] += 1
        else:
            characters[book_characters[i]] = 1
    return characters

def sorted_data(data):
    sorted = []
    for key, value in data.items():
        if key.isalpha():
            sorted.append({"char":key, "num": value})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dict):
    return dict["num"]
