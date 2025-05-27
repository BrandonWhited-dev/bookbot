from stats import get_num_words
from stats import character_nums
from stats import sorted_data
import sys

def get_book_text(path):
    file = ""
    with open(path) as f:
        file = f.read()
    return file

def main():
    if len(sys.argv) < 2:
        #error
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    book_words = get_num_words(book)
    print(f"Found {book_words} total words")
    characters = sorted_data(character_nums(book))
    for i in range(len(characters)):
        print(f"{characters[i]["char"]}: {characters[i]["num"]}")

main()

