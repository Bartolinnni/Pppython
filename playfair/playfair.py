def keyword(word):
    word = word.lower()
    macierz = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    word = ''.join(sorted(set(word), key=word.index))
    word = word[::-1]
    for letter in word:
        if letter == 'j':
            letter = 'i'
        for i in range(len(macierz)):
            if macierz[i] == letter:
                macierz.pop(i)
                macierz.append(letter)
                break
    macierz.reverse()
    def split(a, n):
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

    kwadrat = list(split(macierz,5))
    return kwadrat

def tranform(message):
    index = 0
    for letter in message:
        if letter > 'z' or letter < 'a':
            message = message.replace(letter, '')

    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            message = message + 'x'
            index += 2
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "x" + message[index+1:]
        index +=2   
    return message

def szyfruj(macierz, tekst):
    zaszyfrowany = ''
    tekst.lower()
    for (l1, l2) in zip(tekst[0::2], tekst[1::2]):
        for i in range(5):
            for j in range(5):
                if l1 == macierz[i][j]:
                    row1 = i
                    col1 = j
        for i in range(5):
            for j in range(5):
                if l2 == macierz[i][j]:
                    row2 = i
                    col2 = j
        if(row1 == row2):
            zaszyfrowany += macierz[row1][(col1+1)%5] + macierz[row2][(col2+1)%5]
        elif(col1 == col2):    
            zaszyfrowany += macierz[(row1+1)%5][col1] + macierz[(row2+1)%5][col2]
        else:                
            zaszyfrowany += macierz[row1][col2] + macierz[row2][col1]
    return zaszyfrowany

def odszyfruj(macierz, tekst):
    zaszyfrowany = ''
    tekst.lower()
    for (l1, l2) in zip(tekst[0::2], tekst[1::2]):
        for i in range(5):
            for j in range(5):
                if l1 == macierz[i][j]:
                    row1 = i
                    col1 = j
                    break
        for i in range(5):
            for j in range(5):
                if l2 == macierz[i][j]:
                    row2 = i
                    col2 = j
                    break
        if(row1 == row2):
            zaszyfrowany += macierz[row1][(col1-1)%5] + macierz[row2][(col2-1)%5]
        elif(col1 == col2):    
            zaszyfrowany += macierz[(row1-1)%5][col1] + macierz[(row2-1)%5][col2]
        else:                
            zaszyfrowany += macierz[row1][col2] + macierz[row2][col1]
    return zaszyfrowany




word = input("PODAJ SLOWO KLUCZ: ")

macierz = keyword(word)


with open('tekst.txt') as f:
    lines = f.readlines()

lines = ''.join(lines)
lines = lines.replace('j', 'i')
lines = lines.lower()
lines = tranform(lines)
print(lines)
zaszyfrowany = szyfruj(macierz, lines)

with open('zaszyfrowany.txt', 'w') as f:
    f.write(zaszyfrowany)
odszyfrowany = odszyfruj(macierz, zaszyfrowany)
with open('odszyfrowany.txt', 'w') as f:
    f.write(odszyfrowany)

# word = input("PODAJ SLOWO KLUCZ: ")

# macierz = keyword(word)
# print(macierz)