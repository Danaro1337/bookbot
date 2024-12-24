def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    character_map = get_characters(text)
    print_report(book_path, num_words, character_map )

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_characters(text):
    text_lowercase = text.lower()
    character_map = {}
    for character in text:
        if character not in character_map:
            character_map[character] = 1
        else:
            character_map[character] = character_map[character] + 1
    #sort dict.
    ordered_map = dict(sorted(character_map.items()))
    #print(f"Here is a list of the usage of the different characters: \n{ordered_map}")
    return ordered_map

def print_report(path, count, character_map):
    print(f"Begin report of {path}\n {count} words found in the document")
    for entry in character_map:
        print(f"The character {entry} was found {character_map[entry]}")
    print("end report!")
main()
