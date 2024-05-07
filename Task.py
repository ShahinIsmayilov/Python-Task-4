class Figur:
    def hərəkət_istiqaməti(self):
        pass 

class Piyada(Figur):
    def hərəkət_istiqaməti(self):
        print("Piyada irəli hərəkət edir.")

class At(Figur):
    def hərəkət_istiqaməti(self):
        print("At L formada hərəkət edir.")

class Fil(Figur):
    def hərəkət_istiqaməti(self):
        print("Fil çapraz hərəkət edir.")

class Top(Figur):
    def hərəkət_istiqaməti(self):
        print("Top şaquli və ya səth istiqamətində hərəkət edir.")

class Vəzir(Figur):
    def hərəkət_istiqaməti(self):
        print("Vəzir bütün istiqamətlərə hərəkət edə bilir.")

class Şah(Figur):
    def hərəkət_istiqaməti(self):
        print("Şah hər istiqamətdə bir addım hərəkət edir.")

figurlar = [Piyada(), At(), Fil(), Top(), Vəzir(), Şah()]

print("Şahmat figurları:")
for figur in figurlar:
    figur.hərəkət_istiqaməti()