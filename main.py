def word_appear(file_name):
    word_counter={}
    low_file_name = file_name.lower()
    for word in low_file_name:
        if word in word_counter:
          word_counter[word] += 1
        else: 
          word_counter[word] = 1
   #print(word_counter)
    return word_counter
#puts entire string into lowercase, then splits it, and populates the directory with character counts.

def book_report(file_name):
    char_dict = word_appear(file_name)
    word_counter = word_count(file_name)
    dict_list = []
    for char in char_dict:
       
       dict_list.append({"char": char, "num":char_dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]


def word_count(file_name):
    new_words = []
    count = 0
    new_words = file_name.split()
    for words in new_words:
        count += 1
    #print(count)
    return count
    # counts the words in a file by splitting it and then iterating over the block with a counter
def main():
    
    with open("books/Frankenstein.txt") as f:
     file_contents = f.read()
     #print(file_contents)
     #word_count(file_contents)
     #word_appear(file_contents)
     wordc = word_count(file_contents)
     sorted_list = book_report(file_contents)
     print("--- Begin report of books/frankenstein.txt ---")
     print("f{wordc} words found in the document")
     for item in sorted_list:
        if not item["char"].isalpha():
           continue
        char = item["char"]
        num = item["num"]
        print(f" The {char} character was found {num} times")
     print("--- End report ---")

main()
