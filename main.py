def main():
    book_path = "books/frankenstein.txt"
    book_name = book_path.split('books/')[1].lstrip().split('.')[0].capitalize()
    text = get_book_text(book_path)
    words = word_count(text)
    print(f"--- Begin report of {book_name} ---")
    print(f"{book_name} has: {words} words")
    print()

    letter_report(count_letters(text.lower()))
    print("--- End of Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(word_input):
    words = word_input.split()

    return len(words)

def count_letters(text_input):
    text_dict = {}
    for i in text_input:
        if i.isalpha() == True:
            text_dict[i] = text_dict.get(i, 0) + 1
    new_dict = dict(sorted(text_dict.items(), key=lambda item: item[1], reverse=True))
    return new_dict

def letter_report(text):
    for i in list(text):
        print(f"The '{i}' character was found {text[i]} times")


main()
