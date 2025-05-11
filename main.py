import os
from models import Base, engine

def main():
    db_path = 'Web_prog.db'
    
    # Veritabanı dosyasının var olup olmadığını kontrol et
    if not os.path.exists(db_path):
        print("Veritabanı dosyası bulunamadı, oluşturuluyor...")
        Base.metadata.create_all(engine)  # Veritabanı ve tablolar oluşturuluyor
        print("Veritabanı başarıyla oluşturuldu.")
    else:
        print("Veritabanı dosyası zaten mevcut.")

if __name__ == '__main__':
    main()
