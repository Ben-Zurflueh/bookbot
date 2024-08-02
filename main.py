def main():
    book_path = "books/frankenstein.txt" # path to the book
    text = get_book_text(book_path) # this runs the get book text function
    total_words = word_count(text)  # this runs the word count fuction
    lower = char_count(text) 
    sorted_chars = sort(lower)
    #print(text)   
    # Print the total word count.
    #print(total_words)
    # Print the whole thing in lowercase
    #print(lower)
    print(f'--- Begin report of {book_path} ---')
    print(f'{total_words} words found in the documents')

    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"The {item['char']}' character was found {item['num']} times")
    

def get_book_text(path):
    with open(path) as f: #opens the book txt file and reads it
        return f.read() # returns the text of the book file

def word_count(text): #takes the text as imput from the get book text def
    words = text.split() # splits the words into a list
    return len(words) # returns the lengh of the words list

def char_count(text):
    char_dictionary = {}
    lowered_string = text.lower()
    for i in lowered_string:
        if i in char_dictionary:
            char_dictionary[i] += 1
        else:
            char_dictionary[i] = 1
    return char_dictionary

def sort(lower):
    #Convert dictionary to list of dictionaries
    char_list = [{'char': char, 'num': count} for char, count in lower.items()]

    # A function that returns the 'num' value from a dictionary
    def sort_on(dict):
        return dict['num']
    
    #sort the list in descending order based on 'num'
    char_list.sort(reverse=True, key=sort_on)

    return char_list

main()