with open("sk_50k.txt", encoding="utf-8") as file_words:
    words = file_words.read()
    words_list = [word.split(" ")[0] for word in words.split('\n')]
    print(words_list[0:5001])
# '\n'.join(words_list)
with open('words-list.txt', 'w', encoding="utf-8") as file_words_list:
    file_words_list.write('\n'.join(words_list[0:5000]))
