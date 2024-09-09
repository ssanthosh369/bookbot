def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    print(f"Words in text: {word_count}")
    char_count = get_char_count(text)
    print(f"Characters in text: {char_count}")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    count = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count 


if __name__ == "__main__":
    main()