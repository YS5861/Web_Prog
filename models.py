from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, UniqueConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Veritabanı bağlantısı
engine = create_engine('sqlite:///Web_prog.db', echo=True)
Base = declarative_base()

class Kullanici(Base):
    __tablename__ = 'kullanici'

    ogr_no = Column(Integer, primary_key=True)
    ad = Column(String(50))
    soyad = Column(String(50))
    is_ogretmen = Column(Boolean, default=False)  # Yetki bilgisi: Öğretmen mi?

    katilimlar = relationship("Katilim", back_populates="kullanici")

class PC(Base):
    __tablename__ = 'pc'

    pc_id = Column(Integer, primary_key=True)
    katilimci_sayisi = Column(Integer)

    katilimlar = relationship("Katilim", back_populates="pc")

class Katilim(Base):
    __tablename__ = 'katilim'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ogr_no = Column(Integer, ForeignKey('kullanici.ogr_no', ondelete='CASCADE'))
    pc_id = Column(Integer, ForeignKey('pc.pc_id', ondelete='CASCADE'))
    puan = Column(Integer)

    kullanici = relationship("Kullanici", back_populates="katilimlar")
    pc = relationship("PC", back_populates="katilimlar")

    __table_args__ = (
        UniqueConstraint('ogr_no', 'pc_id', name='uix_ogr_pc'),  # Aynı öğrenci aynı etkinliğe 2 kere katılamaz
    )

# Dizinler (Index) — performans için
Index('idx_ogr_no', Katilim.ogr_no)
Index('idx_pc_id', Katilim.pc_id)
