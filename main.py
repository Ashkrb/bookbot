def word_count(file_name):
    new_words = []
    count = 0
    new_words = file_name.split()
    for words in new_words:
        count += 1
    print(count)
    return count
    # counts the words in a file by splitting it and then iterating over the block with a counter
def main():
    
    with open("books/Frankenstein.txt") as f:
     file_contents = f.read()
     print(file_contents)
     word_count(file_contents)
     
main()
