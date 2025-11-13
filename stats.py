def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_letter_count(content: str):
    letters = {}
    contentLower = content.lower()

    for ch in contentLower:
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] += 1
    return letters


def organise(letters):
    def sort_on(items):
        return items["num"]

    new = []
    for char_key, num_value in letters.items():
        new.append({"char": char_key, "num": num_value})
    new.sort(reverse=True, key=sort_on)
    return new
