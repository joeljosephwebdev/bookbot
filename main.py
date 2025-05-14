import sys
from stats import get_book_text, count_words, char_count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    
    book_path = sys.argv[1]
    if not book_path.endswith('.txt'):
        print("Please provide a valid .txt file.")
        sys.exit(1)
 
    book = get_book_text(book_path)
    print(f"""
--- The book we are analyzing is {book_path} ---
{count_words(book)} words found in the document.

Here is a character frequency breakdown:
""")
    for char, count in char_count(book).items():
        print(f'The {char} character was found {count} times')
