def word_appear(file_name):
    word_counter={}
    low_file_name = file_name.lower()
    word_list = low_file_name.split()
    for word in word_list:
        if word in word_counter:
          word_counter[word] += 1
        else: 
          word_counter[word] = 1
    #print(word_counter)
    return word_counter
#puts entire string into lowercase, then splits it, and populates the directory with word counts.




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
     #print(file_contents)
     word_count(file_contents)
     word_appear(file_contents)
     
main()
