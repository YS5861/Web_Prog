from models import Base, engine

def main():
    # Veritabanı ve tabloları oluşturur
    print("Veritabanı oluşturuluyor...")
    Base.metadata.create_all(engine)
    print("Veritabanı başarıyla oluşturuldu.")

if __name__ == '__main__':
    main()
