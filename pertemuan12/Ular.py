from Animal import Animal

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, warna, Ukuran):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.warna= warna
        self.Ukuran= Ukuran

    def info_Ular(self):
        super().info_animal()
        print("warna \t\t\t: ", self.warna,
            "\nUkuran \t\t\t : ", self.Ukuran)  
          

print("======================================")

Ular_piton = Ular("python", "ikan","amfibi", "bertelur", "kuning", "panjangnya 23 inci")
Ular_piton.info_Ular()

print("=======================================")

Ular_sanca = Ular("sanca", "burung", "amfibi", "bertelur", "hijau", "panjangnya bisa sampai 8-10 meter")
Ular_sanca.info_Ular()