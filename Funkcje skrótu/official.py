from datetime import datetime
from cryptohash import md5, sha256, sha224, sha1, sha384
from random import randint
import matplotlib


def pierwsze2(f):
    tekst = f

    print('=================================')
    tstart = datetime.now()
    hashedmd5 = md5(tekst)
    print("MD5: ")
    print(hashedmd5)
    print('Exection time: ',datetime.now() - tstart , 'lenght: ', len(hashedmd5) )
    
    tstart = datetime.now()
    hashedsha1 = sha1(tekst)
    print('SHA1')
    print(hashedsha1)
    print('Exection time: ', datetime.now() - tstart, 'lenght: ', len(hashedsha1) )


    tstart = datetime.now()
    hashedsha224 = sha224(tekst)
    print('SHA224')
    print(hashedsha224)
    print('Exection time: ', datetime.now() - tstart, 'lenght: ', len(hashedsha224) )


    tstart = datetime.now()
    print('SHA256')
    hashedsha256 = sha256(tekst)
    print(hashedsha256)
    print('Exection time: ', datetime.now() - tstart, 'lenght: ', len(hashedsha256) )


    tstart = datetime.now()
    hashedsha384 =sha384(tekst)
    print('SHA384: ')
    print(hashedsha384)
    print('Exection time: ', datetime.now() - tstart, 'lenght: ', len(hashedsha384) )
    print('-----------------------------------------------------------------')

def losowosc():
    print('\n')
    print('ZAD 6.TEST DLA SKRÓTU SHA1')
    word1 = "Kot"
    word2 = "Kou"
    word3 = "Koc"

    hashed1sha1 = sha1(word1)
    hashed2sha1 = sha1(word2)
    hashed3sha1 = sha1(word3)

    
    hashed1sha1 = int(hashed1sha1,16)
    hashed2sha1 = int(hashed2sha1, 16)
    hashed3sha1 = int(hashed3sha1, 16)

    hashed1sha1 = bin(hashed1sha1)
    hashed2sha1 = bin(hashed2sha1)
    hashed3sha1 = bin(hashed3sha1)

    roznica = 0

    for i in range(len(hashed2sha1)):
        if hashed2sha1[i] == hashed1sha1[i]:
            roznica = roznica + 1
    
    print('Różnica między Kot i Kou wynosi: ',(roznica * 100)/len(hashed1sha1),'%')

    roznica = 0

    for i in range(len(hashed2sha1)):
        if hashed2sha1[i] == hashed3sha1[i]:
            roznica = roznica + 1
    
    print('Różnica między Koc i Kou wynosi: ', (roznica * 100)/len(hashed1sha1),'%')

    roznica = 0

    for i in range(len(hashed2sha1)):
        if hashed3sha1[i] == hashed1sha1[i]:
            roznica = roznica + 1
    
    print('Różnica między Koc i Kot wynosi: ', (roznica * 100)/len(hashed1sha1),'%')


def kolizja():
    counter = 0
    while True:
        counter = counter + 1
        lenword1 = randint(1,10)
        lenword2 = randint(1,10)
        word1 = ''
        word2 = ''
        
        for x in range(lenword1):
            num = randint(0,127)
            word1 = word1 + chr(num)
        
        for x in range(lenword2):
            num = randint(0,127)
            word2 = word2 + chr(num)

        hashed1md5 = md5(word1)
        hashed2md5 = md5(word2)
        hashed1md5 = int(hashed1md5,16)
        hashed2md5 = int(hashed2md5, 16)
        hashed1md5 = bin(hashed1md5)
        hashed2md5 = bin(hashed2md5)
        if hashed1md5[0:11] == hashed2md5[0:11]:
            print('Za', counter,'razem używając skrótu md5 udało się ustalić że te same 12 bitów mają hashe ciągów: ')
            print('word1',word1)
            print('word2 ' ,word2)
            break
        
def main():
    with open("10mb.txt", "r") as file:
        tekst = file.read()

    with open('1mb.txt', 'r') as file:
        tekst1 = file.read()

    with open('5mb.txt', 'r') as file:
        tekst2 = file.read()

    print("DLA 10 mb")
    pierwsze2(tekst)
    print('Dla 1 mb')
    pierwsze2(tekst1)
    print('Dla 5 mb')
    pierwsze2(tekst2)

    losowosc()
    print('\n')
    print('Zadanie 5')
    kolizja()
    
main()