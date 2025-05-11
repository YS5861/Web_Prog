from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

#Burda yazılan kod .db uzantılı bir database dosyası oluşturur.
# Veritabanı bağlantısı
engine = create_engine('sqlite:///Web_prog.db', echo=True)
Base = declarative_base()

# PC tablosu 
class PC(Base):
    __tablename__ = 'pc'

    pc_id = Column(Integer, primary_key=True)
    katilimci_sayisi = Column(Integer)
    puanlar = Column(JSON)  # {"123": 80, "124": 95}

    # Bu etkinliğe katılan öğrenciler
    ogrenciler = relationship("Ogrenci", back_populates="pc")

# Öğrenci tablosu
class Ogrenci(Base):
    __tablename__ = 'ogrenci'

    ogr_no = Column(Integer, primary_key=True)
    ad = Column(String)
    soyad = Column(String)
    pc_id = Column(Integer, ForeignKey('pc.pc_id'))

    pc = relationship("PC", back_populates="ogrenciler")

# Tabloları oluştur
Base.metadata.create_all(engine)
