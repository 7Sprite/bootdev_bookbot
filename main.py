from stats import get_book_text, get_num_words, get_char_occurences, get_charOnly_Occurence
import sys


def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    # dataUrl = "books/frankenstein.txt"
    dataUrl = sys.argv[1]
    content = get_book_text(dataUrl)
    content_count = get_num_words(content)
    char_occurences = get_char_occurences(content)
    char_occurences_sorted = get_charOnly_Occurence(char_occurences)
    print("===========BOOK BOT============")
    print("Analyzing book found at", dataUrl)
    print("---------Word Count----------")
    print(f"Found {content_count} total words")
    print("---------Character Count----------")
    for i in char_occurences_sorted:
        print(f"{i["char"]}: {i["num"]}")
    

if __name__ == "__main__":
    main()