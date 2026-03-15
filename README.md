# Oto Galeri Yönetim Sistemi (Python OOP)

Terminal üzerinden çalışan, nesne yönelimli programlama (OOP) prensipleriyle geliştirilmiş bir araç ve galeri yönetim uygulamasıdır. Birden fazla galeriyi aynı anda yönetmek, araç stoklarını takip etmek ve dinamik bir ID sistemi kurmak amacıyla tasarlanmıştır.

## Proje Hakkında

Bu projede temel amaç, veri yapılarını ve Python'daki sınıf (class) ilişkilerini pratik etmektir. `Car` ve `Gallery` sınıfları birbirleriyle entegre çalışır. Sistemdeki her arabaya, oluşturulduğu anda benzersiz bir ID otomatik olarak atanır. Araç silinse dahi ID sayacı kaldığı yerden devam eder, böylece veri tutarsızlıklarının önüne geçilir.

##  Teknik Özellikler

* **Class ve Instance Yönetimi:** Her galeri kendi içinde bağımsız bir araç listesi (`self.cars`) tutar. 
* **Otomatik ID Atama:** `Car` sınıfı içindeki sınıf değişkeni (`_next_id`) kullanılarak, kullanıcıdan bağımsız ve güvenli bir ID yönetim sistemi kurulmuştur.
* **Dinamik Stok Takibi:** Eklenen araçların stok durumları sonradan güncellenebilir ve yönetilebilir.
* **Hata Yakalama (Try-Except):** Kullanıcı girişlerindeki tip uyuşmazlıkları (örn: sayı yerine harf girilmesi) `ValueError` ile yakalanarak programın çökmesi engellenir.

##  Kurulum ve Kullanım

Herhangi bir harici kütüphane gerektirmez. Sadece Python'un bilgisayarınızda kurulu olması yeterlidir.

1. Repoyu bilgisayarınıza indirin:
   ```bash
   git clone [https://github.com/kullaniciadiniz/oto-galeri-sistemi.git](https://github.com/kullaniciadiniz/oto-galeri-sistemi.git)
