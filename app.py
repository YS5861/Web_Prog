from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from models import engine, Kullanici, PC, Katilim

app = Flask(__name__)
Session = sessionmaker(bind=engine)

# Kullanıcı ekleme (öğrenci veya öğretmen)
@app.route('/kullanici', methods=['POST'])
def kullanici_ekle():
    data = request.json
    session = Session()
    kullanici = Kullanici(
        ogr_no=data['ogr_no'],
        ad=data['ad'],
        soyad=data['soyad'],
        is_ogretmen=data.get('is_ogretmen', False)
    )
    session.add(kullanici)
    session.commit()
    session.close()
    return jsonify({"message": "Kullanıcı eklendi."})

# PC etkinliği ekleme
@app.route('/pc', methods=['POST'])
def pc_ekle():
    data = request.json
    session = Session()
    pc = PC(
        pc_id=data['pc_id'],
        katilimci_sayisi=data['katilimci_sayisi']
    )
    session.add(pc)
    session.commit()
    session.close()
    return jsonify({"message": "PC etkinliği eklendi."})

# Kullanıcının bir etkinliğe katılması ve puan verilmesi
@app.route('/katilim', methods=['POST'])
def katilim_ekle():
    data = request.json
    session = Session()
    katilim = Katilim(
        ogr_no=data['ogr_no'],
        pc_id=data['pc_id'],
        puan=data['puan']
    )
    session.add(katilim)
    session.commit()
    session.close()
    return jsonify({"message": "Katılım ve puan kaydedildi."})

# Kullanıcının tüm katılımlarını listele
@app.route('/kullanici/<int:ogr_no>/katilimlar', methods=['GET'])
def kullanici_katilimlari(ogr_no):
    session = Session()
    katilimlar = session.query(Katilim).filter_by(ogr_no=ogr_no).all()
    sonuc = [{
        "pc_id": k.pc_id,
        "puan": k.puan
    } for k in katilimlar]
    session.close()
    return jsonify(sonuc)

# Tüm kullanıcıları listele
@app.route('/kullanicilar', methods=['GET'])
def kullanicilari_getir():
    session = Session()
    kullanicilar = session.query(Kullanici).all()
    sonuc = [{
        "ogr_no": k.ogr_no,
        "ad": k.ad,
        "soyad": k.soyad,
        "is_ogretmen": k.is_ogretmen
    } for k in kullanicilar]
    session.close()
    return jsonify(sonuc)

if __name__ == '__main__':
    app.run(debug=True)
