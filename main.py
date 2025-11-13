import sys

from stats import get_book_text, get_letter_count, organise


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    content = get_book_text(book)

    words = content.split()
    counts = get_letter_count(content)
    order = organise(counts)

    print(f"Found {len(words)} total words")

    for item in order:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    return


main()
