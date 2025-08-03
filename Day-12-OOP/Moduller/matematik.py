def topla(a,b):
    return a+b

def carp(a,b):
    return a*b

def faktoriyel(n):
    sonuc = 1
    for i in range(1,n+1):
        sonuc *= i
    return sonuc

if __name__ == "__main__":
    print("Test Alanı:")
    print(topla(2,3))
    print(carp(4,5))

    