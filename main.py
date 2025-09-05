import sys
from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_structure(char_count_list):
    for char in char_count_list:
        if  char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
        else:
            continue


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    usr_fl_path = sys.argv[1]
    book_text = get_book_text(usr_fl_path)
    word_count = get_num_words(book_text)
    word_message = f" Found {word_count} total words"
    char_count = get_char_count(book_text)
    sorted_char_count = get_sorted_char_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {usr_fl_path}...")
    print("----------- Word Count ----------")
    print(word_message)
    print("--------- Character Count -------")
    print_structure(sorted_char_count)
    print("============= END ===============")
    

main()
