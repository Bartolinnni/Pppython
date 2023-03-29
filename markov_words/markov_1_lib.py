from random import randint

f = open("norm_wiki_sample.txt", "r")
tekst = f.read()
tekst = tekst[0:100000]

list_of_words = tekst.split(" ")
    
for word in list_of_words:
    if word == "":
        list_of_words.remove(word)
    else:
        for char in word:
            if (ord(char) > 122) or (ord(char) < 97):
                list_of_words.remove(word)
                break

used_words = []
next_words = []
mydict = {}

for index in range(len(list_of_words)):
    if index < len(list_of_words) - 1:

        word_1 = list_of_words[index]
        
        word_2 = list_of_words[index + 1]
    
        try:
            mydict[word_1].append(word_2)
        except:
            mydict[word_1] = []
            mydict[word_1].append(word_2)

# print(mydict)

generated = ["the"]

number = int(input("Podaj z ilu słów ma składać się generowany ciąg: "))

for _ in range(number):
    last_word = generated[-1]
    
    poss_add_words = mydict[last_word]
    added_word = poss_add_words[randint(0, len(poss_add_words) - 1)]
    generated.append(added_word)

print(' '.join(generated))
# print(mydict)