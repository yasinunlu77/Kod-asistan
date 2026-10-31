print("=== DİJİTAL ESER KATALOĞU YÜKLENİYOR ===\n")

# 1. AŞAMA: İç İçe Sözlük (Nested Dictionary) Mimarisinin Kurulması
eser_katalogu = {
    "Dîvân-i Hikmet": {
        "yazar": "Hoca Ahmed Yesevî"
    },
    "Mesnevî": {
        "yazar": "Mevlânâ"
    },
    "Risaletü'n Nushiyye": {
        "yazar": "Yunus Emre"
    }
}

# 2. AŞAMA: Zincirleme Veri Erişimi ve Dinamik Ekleme
ikinci_eser_yazari = eser_katalogu["Mesnevî"]["yazar"]
print(f"Mesnevî adli eserin yazari: {ikinci_eser_yazari}")

print("\n[BİLGİ] 'Dîvân-i Hikmet' eseri için 'tür' bilgisi ekleniyor...")
eser_katalogu["Dîvân-i Hikmet"]["tür"] = "Tasavvuf"
print(f"Güncel Dîvân-i Hikmet Kaydi: {eser_katalogu['Dîvân-i Hikmet']}")

# 3. AŞAMA: .get() Metodu ile Güvenli Veri Sorgulama (KeyError Önleme)
print("\n[SORGULAMA] Risaletü'n Nushiyye eseri için basim yili araniyor...")
basim_bilgisi = eser_katalogu["Risaletü'n Nushiyye"].get("basim_yili", "Basim yili bilgisi bulunamadi.")
print(f"Basim Yili: {basim_bilgisi}")
print("==================================================")


