def main():
    text_name = "books/frankenstein.txt"
    text_file = read_file(text_name)
    print(count_words(text_file))
    
def count_words(text_file):
    words = text_file.split()
    return len(words)
        
def read_file(text_name):
    with open(text_name) as f:
        file_contents = f.read()
        return file_contents

main()