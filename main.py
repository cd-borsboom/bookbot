def main():
    text_name = "books/frankenstein.txt"
    text_file = read_file(text_name)
    print(count_words(text_file))
    print(count_characters(text_file))
    
def count_words(text_file):
    words = text_file.split()
    return len(words)
        
def read_file(text_name):
    with open(text_name) as f:
        file_contents = f.read()
        return file_contents
    
def count_characters(text_file):
    text_file_lowerstrings = text_file.lower()
    character_dict = {}
    for character in text_file_lowerstrings:
        if character not in character_dict:
            character_dict.update({character: 1})
        else:
            character_dict[character] += 1
    return character_dict

main()