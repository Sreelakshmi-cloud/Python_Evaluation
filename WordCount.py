def word_count(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    text = text.lower()

    for char in ['.', ',', '!', '?', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}', '"', "'"]:
        text = text.replace(char, ' ')
    
    words = text.split()

    word_count_dict = {}

    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    for word, count in word_count_dict.items():
        print(f"{word}: {count}")

filename = 'wordcount.txt'
word_count(filename)
