class Mobil:
    def __init__(self, merek, model, tahun, warna):  
        self.__merek = merek
        self.__model = model
        self.__tahun = tahun
        self.__warna = warna


    def get_merek(self):
         return self.__merek
    
    def set_merek(self, merek):
        self.__merek = merek
    
    def get_model(self):
         return self.__model
    
    def set_model(self,model):
        self.__model = model
    
    
    def maju(self):
        print(f"{self.__merek} {self.__model} {self.__tahun} {self.__warna} bergerak maju.")
        
    def mundur(self):
        print(f"{self.__merek} {self.__model} {self.__tahun} {self.__warna} bergerak mundur.")
        
    def belok_kanan(self):
        print(f"{self.__merek} {self.__model}  {self.__tahun} {self.__warna}belok kanan.")
        
    def belok_kiri(self):
        print(f"{self.__merek} {self.__model} {self.__tahun} {self.__warna} belok kiri.")


mobil_baru = Mobil("Toyota", "Avanza", 2020, "Hitam")

print("Merek mobil:", mobil_baru.get_merek())
print("Model mobil:", mobil_baru.get_model())

mobil_baru.set_merek("Chevrolet")
mobil_baru.set_model("Camaro")

print("Merek mobil setelah diubah:", mobil_baru.get_merek())
print("Model mobil setelah diubah:", mobil_baru.get_model())

mobil_baru.maju()
mobil_baru.mundur()