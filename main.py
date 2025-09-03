def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(book_text):
    word_count = len(book_text.split())
    return word_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(book_text)
    word_message = f"{num_words} words found in the document"
    print(word_message)
main()






