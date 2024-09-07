import string

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def char_count(text: str) -> dict:
    character_count = {char: 0 for char in string.ascii_lowercase}
    
    for char in text:
        char_lower = char.lower()
        if char_lower in character_count:
            character_count[char_lower] += 1
    
    return sort_dict(character_count)

def sort_dict(dictionary: dict) -> dict:
    # Sort the dictionary by values in descending order
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


if __name__ == '__main__':
    book_path = 'books/frankenstein.txt'
    book = get_book_text(book_path)
    print(f"""
--- The book we are analyzing is {book_path} ---
It has {count_words(book)} words.

Here is a character frequency breakdown:
""")
    for char, count in char_count(book).items():
        print(f'The {char} character was found {count} times')
