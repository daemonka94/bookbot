def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print("---- Begin report of book/frankenstein.txt ----")

    # Add a blank line for separation.
    print()
    
    # Call get_num_words to find out how many words are in the book.
    num_words = get_num_words(text)
    print(f"There are {num_words} words in this book.")

    # Add a blank line for separation.
    print()

    # Call count_each_char to count how many times each character is found in the book.
    character_counts = count_each_char(text)

    # Conver this dictionary into a LIST of dictionaries, sorted by letters
    char_count_list = [{'character': key, 'num': value} for key, value in character_counts.items()]

    # Sort the characters
    char_count_list.sort(reverse=True, key=sort_on)

    # Print sorted characters
    for item in char_count_list:
        print(f"The '{item['character']}' character was found {item['num']} times")

    print()

    print("---- End of report! ----")

def get_num_words(text):
    words = text.split()
    return len(words) 

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_each_char(text):
    lowered_string = text.lower()

    char_count = {}
    for char in lowered_string:
        if char.isalpha():
            if char in char_count:
             char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def sort_on(char_count):
    return char_count["num"]

main()