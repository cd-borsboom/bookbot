def main():
    text_name = "books/frankenstein.txt"
    count_words(text_name)
    
def count_words(text_name):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))
        
main()