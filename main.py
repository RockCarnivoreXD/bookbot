from stats import get_num_words
from stats import get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    word_message = f"{word_count} words found in the document"
    char_count = get_char_count(book_text)
    print(word_message)
    print(char_count)

main()






