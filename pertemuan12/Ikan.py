from Animal import Animal

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak,sirip_ekor, warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.sirip_ekor= sirip_ekor
        self.warna= warna

    def info_ikan(self):
        super().info_animal()
        print("sirip_ekor \t\t: ", self.sirip_ekor,
            "\nwarna \t\t\t : ", self.warna)  
        
print("==========================================")

Ikan_Mas = Ikan("Mas", "cacing", "sungai", "Bertelur", "berlekuk tunggal", "Merah")
Ikan_Mas.info_ikan()

print("===========================================")

Ikan_lele = Ikan("Lele", "Pelet", "Rawa", "Bertelur", "sirip tunggal", "hitam")
Ikan_lele.info_ikan()

