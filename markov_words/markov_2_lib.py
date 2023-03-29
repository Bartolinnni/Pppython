#poprawiony kod

from random import randint

f = open("norm_wiki_sample.txt", "r")
tekst = f.read()
tekst = tekst[0:1000000]
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
    if index < len(list_of_words) - 2:

        word_1 = list_of_words[index]
        
        word_2 = list_of_words[index + 1]
        
        word_3 = list_of_words[index + 2]

        chain = word_1 + " " + word_2 #dodana zmiana
    
        try:
            mydict[chain].append(word_3)
        except:
            mydict[chain] = []
            mydict[chain].append(word_3)

# print(mydict)

generated = ["the", "tragedy"]

number = int(input("Podaj z ilu słów ma składać się generowany ciąg: "))

for _ in range(number):
    index = -2 
    last_word_1 = generated[-2]
    last_word_2 = generated[-1]

    chain = last_word_1 + " " + last_word_2 #dodana zmiana
    poss_add_words = None
    while poss_add_words == None:
        try:
            poss_add_words = mydict[chain]
        except:
            index = index - 1
            last_word_1 = generated[index]
            chain = last_word_1 + " " + last_word_2 #dodana zmiana
    
    added_word = poss_add_words[randint(0, len(poss_add_words) - 1)]
    generated.append(added_word)

print(' '.join(generated))
# print(mydict)