def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    """
    Counts the frequency of each alphabetic character in the string (case insensitive).
    """
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():  # Count only alphabetic characters
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def print_report(book_path, num_words, chars_dict):
    """
    Prints a formatted report of the word count and character frequencies.
    """
    # Sort characters by frequency in descending order
    sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)

    # Print the report header
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    # Print the character frequencies
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    # Print the report footer
    print("--- End report ---")


main()
