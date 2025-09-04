def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

def get_char_count(book_text):
    char_count = {} 
    low_case_words = book_text.lower()
    for char in low_case_words:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    return char_count["num"]

def get_sorted_char_counts(char_count):
    char_count_list = [{"char": char, "num": num} for char, num in char_count.items()]

    char_count_list.sort(reverse= True, key=sort_char_count)
    return char_count_list