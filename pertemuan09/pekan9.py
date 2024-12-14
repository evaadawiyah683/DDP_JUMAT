
#soal 1
#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))   
# Output: 32.0
#print(celcius_ke_fahrenheit(100))  
# Output: 212.0

def celcius_ke_fahreint(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

print(f"Hasilnya adalah {celcius_ke_fahreint(0)}")
print(celcius_ke_fahreint(100))

#soal 2
#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  
# Output: True
#print(is_genap(7))
# Output: False

def is_genap(angka):
    return angka % 2 == 0

print(is_genap(4))
print(is_genap(13))

print("================================")


#soal 3
#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal

def nilai_kelulusan(nilai):
    print()
    if nilai >= 80:
        return 'lulus'
    else :
        return 'gagal'



print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

print("================================")

#soal 4
#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,19

def bilangan(n):
    for i in range(1, n):
        if i % 2 != 0:
            print(i, end=", ")
    print()
bilangan(20)

print("===============================")

#ini tantangan kalau bisa pulang
#output syamil bisa pulang kalau 

def ddp(ketentuan):
    if ketentuan =="bisa":
        print("syamil pulang")
    elif ketentuan =="gagal":
        print("syamil ga pulang")
    else:
        print("inputan tidak valid")  
ddp("bisa")         

 










