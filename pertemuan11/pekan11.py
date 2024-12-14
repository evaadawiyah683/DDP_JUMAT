class Orang:
    # variabel (properti)
    nama = "zilong"
    umur = 0
    gender = ""
    

    #fungsi(method)
    def ngomong(self):
        print("saya bisa berberbicara")

    def jalan(self, kata):
        print("saya bisa jalan",kata)
# objek1
supir = Orang()
supir.nama = "Agus"
print(supir.nama)
supir = Orang()
print(supir.nama)
supir.jalan("kapan?")
supir.sim ="A"
print(supir.sim) 

mahasiswa = Orang()
print("mahasiswa.nama")
