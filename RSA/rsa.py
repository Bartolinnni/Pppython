from random import randint
import sympy
import math

def pick_num(num):
    prime = sympy.nextprime(num)
    return prime

def e_generating(num):
    e = randint(1, num)
    while math.gcd(e,num) != 1:
        e = randint(1, num)
    return e


def szyfrowanie(m, e, n):
    zaszyfrowane = []
    for char in m:
        num = ord(char)
        c = pow(num, e, n)
        zaszyfrowane.append(c)
    return zaszyfrowane

def deszyfrowanie(c,d,n):
    odszyforwane = ""
    for element in c:
        m = pow(element, d, n)
        odszyforwane = odszyforwane + chr(m)
    return odszyforwane

def main():
    p_x = randint(1000,9000)
    q_x = randint(1000,9000)
    p = pick_num(p_x)
    q = pick_num(q_x)
    N = p*q
    phi = (p - 1) * (q - 1)
    e = e_generating(phi)
    d = pow(e, -1, phi)
    slowo = input("Podaj słowo: ")
    zaszyfrowane = szyfrowanie(slowo, e, N)
    slowo_odszyfrowane = deszyfrowanie(zaszyfrowane, d, N)
    print(zaszyfrowane)
    print(slowo_odszyfrowane)
    # print(zaszyfrowane)

main()