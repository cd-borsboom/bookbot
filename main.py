def main():
    text_name = "books/frankenstein.txt"
    text_file = read_file(text_name)
    
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{count_words(text_file)} words found in the document\n")
    
    how_many_char_sorted = count_characters(text_file)
    print(sorted(how_many_char_sorted.items()))
    # print(count_characters(text_file))
    # print(how_many_char_sorted)
    
    
    
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