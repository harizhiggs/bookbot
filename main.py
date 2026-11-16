from stats import count_words, count_characters, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_report(path_to_file, word_count, sorted_list):    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for tup in sorted_list:
        if tup[0].isalpha():
            print(f"{tup[0]}: {tup[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])   
        char_count = count_words(text)
        characters = count_characters(text)
        s_characters = chars_dict_to_sorted_list(characters)
        print_report(sys.argv[1], char_count, s_characters)

main()