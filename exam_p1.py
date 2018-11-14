import string
names = []
name_val = {}
words = []
words_val = {}

def load_roster(file_name):
    file = open(file_name, 'r')
    line = file.readline()
    for line in file:
        first_name = line.split()[0]
        names.append(first_name)
    file.close()
    return names

def load_words(file_name):
    file = open(file_name, 'r')
    line = file.readline()
    for line in file:
        word = line.split()[0]
        if '-' in word:
            word = line.replace('-','').split()[0]
        words.append(word)
    file.close()
    return words
    
def load_positive_words():
    with open("./positive-words.txt") as f:
        positive_words = f.readlines()
    positive_words = [x.strip() for x in positive_words] 
    return positive_words

def add_words(my_list = []):
    lower = string.ascii_lowercase
    for word in my_list:
        total_low = 0
        for letter in word:
            x = lower.index(letter) + 1
            total_low += x
        words_val[word] = total_low
    return words_val

def add_names(my_list = []):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    for name in my_list:
        total_low = 0
        total_up = 0
        for letter in name:
            if letter in lower:
                a = lower.index(letter) + 1
                total_low += a
            else:
                b = upper.index(letter) + 1
                total_up += b
        name_val[name] = total_low + total_up
    return name_val

def find_name(my_dict = {}):
    max_value = max(my_dict.values())
    for name, value in my_dict.items():
        if max_value == value:
            return name

def find_word(my_dict = {}):
    my_value = 60
    my_words = []
    for word, val in my_dict.items():
        if val == my_value:
            my_words.append(word)
    return my_words

        
def main():
    load_roster('roster.txt')
    add_names(names)
    # print(name_val)
    print('Here is the student with the most value:')
    print(find_name(name_val))
    load_words('positive-words.txt')
    add_words(words)
    print('Here are the words with the same value as the name "Connie":')
    print(find_word(words_val))
    
    


if __name__ == '__main__':
    main()
