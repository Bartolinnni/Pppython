import sympy
from random import randint

# def search_for_pr(n):
#     list_of_pr = []
#     for x in range(2,n):
#         potential = is_pr(n,x)
#         if potential == 1: pass
#         else: list_of_pr.append(potential)
#     return list_of_pr

def is_pr(n, g):
    list_pow = []
    for i in range(1, n):
        x = pow(g, i, n)
        if list_pow.count(x) >= 1:
            break
        else:
              list_pow.append(x)
    if len(list_pow) == n - 1:
        return g
    else:
        return 1

n = int(input("Podaj dowolną liczbę 4 cyfrową: "))
if sympy.isprime(n) == False:
    n = sympy.nextprime(n)
    print("Wprowadzona przez ciebie liczba nie jest liczbą pierwszą dlatego twoje n jest równe: ", n)
# print(n)
# lista_of_pr = search_for_pr(n)
# 
# g = int(input("Wybierz jedną z powyższych liczb jako g: "))
g = int(input("Wybierz pierwiastek pierwotny modulo	n, i gdzie 1<g<n: "))
g = is_pr(n,g)
while g <= 1 or g > n:
    g = int(input("Wybierz pierwiastek pierwotny modulo	n, i gdzie 1<g<n: "))
    g = is_pr(n,g)

x = int(input("A podaj losową liczbe całkowitą większą od 1000: "))
while x < 1000:
    x = int(input("A podaj losową liczbe całkowitą większą od 1000"))

y = int(input("B podaj losową liczbe całkowitą większą od 1000: "))
while y < 1000:
    y = int(input("B podaj losową liczbe całkowitą większą od 1000: "))

X = (g**x)%n
Y = (g**y)%n

print("X = ", X)
print("Y = ", Y)

k_A = (Y**x)%n
k_B = (X**y)%n

print("klucz sesji = ", k_A)
print("klucz sesji = ",k_B)