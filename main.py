def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = word_count(text)  
    # Print the text of the book.
    print(text)   
    # Print the total word count.
    print(total_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text): #takes the text as imput from the get book text def
    words = text.split() # splits the words into a list
    return len(words) # returns the lengh of the words list

main()