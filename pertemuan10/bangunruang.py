import math

#deklarasi fungsi
def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*l)+(l*t)
    print(f'luas balok adalah{hitung}')

def l_kubus(sisi):
    hitung = 6 * sisi ** 2
    print(f'luas kubus adalah {hitung}')

def l_tabung(phi, jari_jari, tinggi):
    hitung = 2 * 3.14 * (jari_jari + tinggi)
    print(f'luas tabung adalah {hitung}')
    
def l_limas_segitiga(tinggi_alas, alas, tinggi1, tinggi2, tinggi3):
    luas_alas = 1/2 * tinggi_alas * alas
    total_l_tegak = 1/2 * alas * tinggi1 + 1/2 * alas * tinggi2 + 1/2 * alas * tinggi3
    hitung = luas_alas + total_l_tegak
    print(f'luas limas adalah {hitung}')  

def l_prisma(alas, tinggi_segitiga, tinggi_prisma, p1, p2, p3):
    hitung =  alas * tinggi_segitiga + ((p1 + p2 + p3) * tinggi_prisma)
    print(f'luas prisma adalah {hitung}')