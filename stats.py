def count_book(text):
    word = text.split()
    return len(word)

def count_character(text):
    count = {}

    for letter in text:
        if letter == " ":
            continue
        letter = letter.lower()

        if letter not in count:
            count[letter] = 1
        elif letter in count:
            count[letter] += 1
        
    return count

def sort_dict(char_count):
    sorted_items = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_items
