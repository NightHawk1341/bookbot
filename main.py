import sys
from stats import turn_to_words
from stats import count_characters
from stats import sorted_characters
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_contents = get_book_text(sys.argv[1])
        result = turn_to_words(book_contents)
        char_count = count_characters(book_contents)
        sorted_chars = sorted_characters(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {result} total words")
        print("--------- Character Count -------")
        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")
main()
