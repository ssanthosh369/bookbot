def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_list = convert_dict(char_count)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    
    for i in char_list:
        if i['char'].isalpha():
                print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")

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

def convert_dict(char_count):
    char_list = [{"char": key, "num": value} for key, value in char_count.items()]
    char_list.sort(reverse=True, key= lambda char_list: char_list["num"])
    
    return char_list

if __name__ == "__main__":
    main()