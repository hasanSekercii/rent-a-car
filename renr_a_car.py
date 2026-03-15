class Car:
    _next_id = 1

    def __init__(self, brand: str, model: str) -> None:
        self.id = Car._next_id
        Car._next_id += 1
        self.brand = brand.strip().title()
        self.model = model.strip().title()
        self.stock = 0

    def add_stock(self, amount: int) -> None:
        if amount > 0:
            self.stock += amount

    def __repr__(self) -> str:
        return f"Car#{self.id} {self.brand} {self.model} (stok: {self.stock})"


class Gallery:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> Car:
        self.cars.append(car)
        return car

    def remove_car(self, car_id: int) -> bool:
        for i, c in enumerate(self.cars):
            if c.id == car_id:
                del self.cars[i]
                return True
        return False

    def add_stock(self, car_id: int, amount: int) -> bool:
        for c in self.cars:
            if c.id == car_id:
                c.add_stock(amount)
                return True
        return False

    def __repr__(self) -> str:
        return f"Gallery[{self.name}] ({len(self.cars)} araba)"


# Galerilerin depolandığı ve erişebileceğimiz bir liste
galeriler = []


def main() -> None:
    # Bir galeri oluştur
    while True:
        try:
            choice = int(input("1-Çıkış\n2-Galeriye Ekle\n3-Galeri Oluştur\n4-Galeri Görüntüle\n5-Ana menü\nLütfen yapmak istedğiniz işlemi seçiniz: ").strip())
        except ValueError:
            print("Geçerli bir sayı giriniz!")
            continue
                
        if choice == 1:
            #çıkış kısmı
            print("Çıkış yapılıyor..")
            break

        elif choice == 2:
            ## Galeri seçip seçilen galeriye araba ekleme 
            if not galeriler:
                # eğer hiç galeri yoksa uyarı verip menüye gönderme
                print("Hiç Galeri Yok! Lütfen önce galeri oluşturun..")
                continue
            else:
                # Galerileri ekrana bastırma ve oradan seçimi alma
                print("Galeriler: ")
                for g in galeriler:  
                    print("-",g.name.title())

            choice2 = input("Lütfen bir galeri seçin: ").strip().title()
            seçilen = None
            for g in galeriler:
                if g.name.title() == choice2:
                    seçilen = g
                    break

            if seçilen is None:
                print("Galeri bulunamadı!!")
                continue
            print(f"{seçilen.name} galerisine girildi..")
            # Kullanıcıdan araba bilgilerini al ve ekle
            print ("eklemek istediğiniz arbanın özellikleri: ")
            marka = input("Marka: ")
            model = input("Model: ")
            eklenen = seçilen.add_car(Car(marka, model))
            print("Eklendi:", eklenen)

            # İsteğe bağlı stok ekleme
            s = input("Stok ekle (sayı, boş geçilebilir): ").strip()
            if s:
                try:
                    amt = int(s)
                    seçilen.add_stock(eklenen.id, amt)
                    print("Stok eklendi.")
                except ValueError:
                    print("Geçersiz sayı.")

            # İsteğe bağlı silme
            s = input("Silmek için ID gir (boş geçilebilir): ").strip()
            if s:
                try:
                    cid = int(s)
                    print("Silme sonucu:", "Başarılı" if seçilen.remove_car(cid) else "Bulunamadı")
                except ValueError:
                    print("Geçersiz ID.")

            # Kalan arabaları yazdır
            print("Kalan arabalar:")
            if not seçilen.cars:
                print("(yok)")
            else:
                for c in seçilen.cars:
                    print("-", c)

        elif choice == 3:
            ##Galeri oluşturulması
            name = input("Lütfen galeri ismi girin: ")
            galeri = Gallery(name)
            galeriler.append(galeri)
            print(f"{name} Galerisi oluşturuldu.")

        elif choice == 4:
            ## Galerilerin görüntülenmesi
            print("Galeriler: ")
            for g in galeriler:  
                print("-",g.name.title())

        elif choice == 5:
            ##
            print("burası yapım aşamasında") 
        else:
            print("lütfen geçerli bir işlem seçin!! ")


if __name__ == "__main__":
    main()
