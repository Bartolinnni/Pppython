from datetime import datetime
from cryptohash import md5, sha256, sha224, sha1, sha384
from random import randint
import matplotlib.pyplot as plt


def ploting(listay, listax, titile):
    plt.plot(listay, listax)
    plt.title(titile)
    # plt.show()


def timemeasure(fun):
    lista1 = []
    lista5 = []
    lista10 = []
    with open('1mb.txt', 'r') as file:
        text1 = file.read()

    with open('5mb.txt', 'r') as file:
        text5 = file.read()

    with open('10mb.txt', 'r') as file:
        text10 = file.read()
    roznica = 0
    print('=================================')
    for i in range(3):
        tstart = datetime.now()
        
        hashed = fun(text1)
        roznica = datetime.now() - tstart
        print('Exection time: ',roznica.microseconds , 'lenght: ', len(hashed))
    
        lista1.append(roznica.microseconds)
    
    for i in range(3):
        tstart = datetime.now()
        
        hashed = fun(text5)
        roznica = datetime.now() - tstart
        print('Exection time: ',roznica.microseconds , 'lenght: ', len(hashed))
    
        lista5.append(roznica.microseconds)

    for i in range(3):
        tstart = datetime.now()
        
        hashed = fun(text10)
        roznica = datetime.now() - tstart
        print('Exection time: ',roznica.microseconds , 'lenght: ', len(hashed))
    
        lista10.append(roznica.microseconds)
    
    return lista1, lista5, lista10, len(hashed)





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

    losowosc()
    print('\n')
    print('Zadanie 5')
    kolizja()
    lista1md5,lista5md5,lista10md5,lenmd5 = timemeasure(md5)
    lista1sha256, lista5sha256, lista10sha256,len256 = timemeasure(sha256)
    lista1sha224, lista5sha224, lista10sha224, len224 = timemeasure(sha224)
    lista1sha1, lista5sha1, lista10sha1, lensha1 = timemeasure(sha1)
    lista1sha384, lista5sha384, lista10sha384, len384 = timemeasure(sha384)
    ploting([1,5,10], [sum(lista1md5)/3, sum(lista5md5)/3, sum(lista10md5)/3], 'MD5 ploting')
    ploting([1,5,10], [sum(lista1sha256)/3, sum(lista5sha256)/3, sum(lista10sha256)/3], 'SHA256 ploting')
    ploting([1,5,10], [sum(lista1sha224)/3, sum(lista5sha224)/3, sum(lista10sha224)/3], 'SHA224 ploting')
    ploting([1,5,10], [sum(lista1sha1)/3, sum(lista5sha1)/3, sum(lista10sha1)/3], 'SHA1 ploting')
    ploting([1,5,10], [sum(lista1sha384)/3, sum(lista5sha384)/3, sum(lista10sha384)/3], 'SHA384 ploting')
    plt.title('Zestawienie wszystkich funkcji skrótu')
    plt.legend(['MD5','SHA256','SHA224','SHA1','SHA384'])
    plt.show()
main()