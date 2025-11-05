from stats import count_book
from stats import count_character
from stats import sort_dict
import sys

def get_book_text(file_path):
    book_contents = ""
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents

def display(path,count,sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for key,value in sorted_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")
        elif not key.isalpha():
            continue
    print("============= END ===============")

def main():
    #path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    count = count_book(text)
    characters_count = {}
    characters_count = count_character(text)
    sorted_dict = {}
    sorted_dict = sort_dict(characters_count)
    display(path,count,sorted_dict)
    
if __name__ == "__main__":
    main()