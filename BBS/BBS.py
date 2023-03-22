from random import randint
from sympy import *
import math


def pick_number(num):
    number = nextprime(num)
    while number%4 != 3:
        number = nextprime(number)
    return number

def searching_for_x(num):
    while True:
        x = randint(900000,1000000)
        if math.gcd(num,x) == 1:
            break
    return x
def generating(range1, x, N):
    chain = ""
    for _ in range(range1):
        x = x**2 % N
        bit = x % 2
        chain = chain + str(bit)
    return chain

def test_poj_bit(chain):
    ilosc_zer = chain.count("0")
    ilosc_jed = chain.count("1")
    print("========TEST 1=========")
    print("Ilość zer w ciągu bitów wynosi: ", ilosc_zer)
    print("Ilość jedynek w ciągu bitów wynosi: ", ilosc_jed)
    if (9725 < ilosc_zer < 10275) and (9725 < ilosc_jed < 10275):
        print("Test pojedyńczych bitów zakończył się sukcesem.")
    
def test_serii(chain):
    ser_len = 0
    list_len = []
    for bit in chain:
        if bit == "1":
            ser_len = ser_len + 1
        elif bit == "0" and ser_len != 0:
            list_len.append(ser_len)
            ser_len = 0
        else: pass
    
    ser_1 = list_len.count(1)
    ser_2 = list_len.count(2)
    ser_3 = list_len.count(3)
    ser_4 = list_len.count(4)
    ser_5 = list_len.count(5)
    ser_rest = len(list_len) - (ser_1 + ser_2 + ser_3 + ser_4 + ser_5)
    print("=========TEST 2===========")
    print("Ciąg bitów: \n", 
          '"1" występuje ',ser_1, " razy\n", 
          '"11" występuje ',ser_2, " razy\n"
          ,'"111" występuje ',ser_3, " razy\n"
          ,'"1111" występuje ',ser_4, " razy\n"
          ,'"11111" występuje ',ser_5, " razy\n",
          'ciągi 1 dłuższe niż 5 występują ',ser_rest, " razy")
    
    if (2315 < ser_1 < 2685) and (1114 < ser_2 < 1386) and (527 < ser_3 < 723) and (240 < ser_4 < 384) and (103 < ser_5 < 209) and (103 < ser_rest < 209):
        print("Test serii zakończył się sukcesem.")
    else: print("Test serii zakończył się porażką.")

def test_dlugiej_serii(chain):
    seria1 = "1"
    seria0 = "0"
    while True:
        if chain.count(seria1) > 0:
            seria1 = seria1 + "1"
        else:
            break
    while True:
        if chain.count(seria0) > 0:
            seria0 = seria0 + "0"
        else:
            break
    longest1 = len(seria1)
    longest0 = len(seria0)
    print("========TEST 3=========")
    print("Najdłuższy ciąg jedynek wynosi: ", longest1)
    print("Najdłuższy ciąg zer wynosi: ", longest0)
    if (longest1 < 26) and (longest0 < 26):
        print("Test długiej serii zakończył się sukcesem.")

def poker_test(chain):
    com_list = ["0000","0001","0010","0011","0100","0101","0110","0111","1000", "1001","1010","1011","1100","1101","1110","1111"]
    tab_seg = []
    str_count = []
    for i in range(16):
        str_count.append(0)

    for (b0,b1,b2,b3) in zip(chain[0::4], chain[1::4], chain[2::4], chain[3::4]):
        str = b0 + b1 + b2 + b3
        tab_seg.append(str)
    print("========TEST 4=========")
    for i in range(16):
        str_count[i] = tab_seg.count(com_list[i])
        print("Ciąg bitów: ", com_list[i], "występuje ", str_count[i], " razy")
    
    result_x = 0
    for i in range(16):
        result_x += str_count[i] ** 2
    result = (result_x * (16 / 5000)) - 5000
    print("Wynik: ", result)
    if 2.16 < result < 46.17:
        print("Test pokerowy zakończył się sukcesem.")
    else:
        print("Test pokerowy zakończył się porażką.")

def main():
    x_p = randint(3*10**10,4*10**10)
    x_q = randint(3*10**10,4*10**10)
    p = pick_number(x_p)
    q = pick_number(x_q)
    N = p * q
    x = searching_for_x(N)
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"N = {N}")
    print(f"x = {x}")
    chain = generating(20000, x, N)
    test_poj_bit(chain)
    test_serii(chain)
    test_dlugiej_serii(chain)
    poker_test(chain)

main()