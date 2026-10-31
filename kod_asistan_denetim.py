# KOD-ASISTAN PROJESİ v1.3 (STANDART DIŞI YAPAY ZEKÂ ÇIKTISI)
print("=== KOD-ASISTAN: YAPAY ZEKÂ STANDART DIŞI KOD HAVUZU ===\n")

# YÖNETİCİ GİRİŞİ KATMANI (Tekrar Eden Blok 1)
print("[SİSTEM] Yönetici erişim katmani doğrulaniyor...")
sepet_1 = 600
if sepet_1 > 500:
    net_1 = sepet_1 * 0.90
    print(f"Yönetici için indirim uygulandi. Ödenecek: {net_1} TL")
else:
    print(f"Yönetici için indirim yok. Ödenecek: {sepet_1} TL")

# ÖĞRETMEN GİRİŞİ KATMANI (Tekrar Eden Blok 2)
print("[SİSTEM] Öğretmen erişim katmani doğrulanıyor...")
sepet_2 = 450
if sepet_2 > 500:
    net_2 = sepet_2 * 0.90
    print(f"Öğretmen için indirim uygulandi. Ödenecek: {net_2} TL")
else:
    print(f"Öğretmen için indirim yok. Ödenecek: {sepet_2} TL")

# ÖĞRENCİ GİRİŞİ KATMANI (Tekrar Eden Blok 3)
print("[SİSTEM] Öğrenci erişim katmani doğrulaniyor...")
sepet_3 = 800
if sepet_3 > 500:
    net_3 = sepet_3 * 0.90
    print(f"Öğrenci için indirim uygulandi. Ödenecek: {net_3} TL")
else:
    print(f"Öğrenci için indirim yok. Ödenecek: {sepet_3} TL")


    