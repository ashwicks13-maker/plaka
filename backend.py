# -*- coding: utf-8 -*-
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# JSON dosyasını yükle
with open("plakalar.json", "r", encoding="utf-8") as f:
    veriler = json.load(f)

@app.route("/")
def home():
    return jsonify({
        "durum": "aktif",
        "endpointler": {
            "ad": "/ad?isim=OĞUZHAN",
            "soyad": "/soyad?soyad=UĞUR",
            "adsoyad": "/adsoyad?isim=OĞUZHAN UĞUR",
            "plaka": "/plaka?plaka=34KG4978"
        }
    })

# AD ile sorgu
@app.route("/ad")
def ad_sorgu():
    isim = request.args.get("isim", "").upper()

    sonuc = [
        kisi for kisi in veriler
        if isim in kisi["isim"].upper().split()
    ]

    return jsonify(sonuc)

# SOYAD ile sorgu
@app.route("/soyad")
def soyad_sorgu():
    soyad = request.args.get("soyad", "").upper()

    sonuc = [
        kisi for kisi in veriler
        if kisi["isim"].upper().split()[-1] == soyad
    ]

    return jsonify(sonuc)

# AD SOYAD ile sorgu
@app.route("/adsoyad")
def adsoyad_sorgu():
    isim = request.args.get("isim", "").upper()
    soyad = request.args.get("soyad", "").upper()

    tam_ad = f"{isim} {soyad}"

    sonuc = [
        kisi for kisi in veriler
        if kisi["isim"].upper() == tam_ad
    ]

    return jsonify(sonuc)

# PLAKA ile sorgu
@app.route("/plaka")
def plaka_sorgu():
    plaka = request.args.get("plaka", "").upper()

    sonuc = [
        kisi for kisi in veriler
        if kisi["plaka"].upper() == plaka
    ]

    return jsonify(sonuc)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
