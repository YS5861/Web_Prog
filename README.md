# Web_Prog

24-25 Web Programa Dersi Dönem Ödevi

## 🔹 1. models.py — Veritabanı Modeli

Bu dosya, sistemde kullanılacak veritabanı tablolarının tanımını yapar.

### İçeriği:

- **Kullanici**: Sistemdeki tüm kullanıcıları temsil eder. Öğrenci ya da öğretmen olabilir.

  - `ogr_no`: Öğrenci numarası (birincil anahtar)
  - `ad`, `soyad`: Ad ve soyad bilgileri
  - `is_ogretmen`: Bu kişi öğretmen mi? (True/False)

- **PC**: Etkinlik (Programlama Çalışması) tablosudur.

  - `pc_id`: Etkinlik kimliği
  - `katilimci_sayisi`: Kaç kişi katıldı?

- **Katilim**: Kullanıcının bir etkinliğe katıldığını ve aldığı puanı tutar.
  - `ogr_no`, `pc_id`: Hangi kullanıcı, hangi etkinliğe katıldı?
  - `puan`: Etkinlikten aldığı puan
  - Aynı kullanıcı aynı etkinliğe birden fazla kez katılamaz (tekil kısıt uygulanır).
