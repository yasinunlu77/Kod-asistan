# Geliştirici: [Öğrenci Adı Soyadı]
print("=== KOD-ASİSTAN: DİNAMİK SEPET YÖNETİM PANELİ ===")
print("NOT: Ürün fiyatlarini sirayla giriniz. Veri girişini bitirmek için 'HESAPLA' yaziniz.\n")

# 1. AŞAMA: Bellekte boş dinamik listenin tanımlanması
sepet_listesi = [ ]

# 2. AŞAMA: Kesintisiz Veri Toplama Döngüsü (while)
while True:
    girdi = input("Ürün Fiyati veya Komut: ").strip()
    
    # Harf Duyarlılığının Çözülmesi ve Çıkış Protokolü
    if girdi.upper() == "HESAPLA":
        print("Veri girişi sonlandirildi. Hesaplama katmanina geçiliyor...")
        # KONTROL İFADESİ: Veri giriş döngüsü kırılır.
        break
    
    # Sayısal Dönüşüm ve Kararsız Veri Giriş Filtresi
    else:
        # Metinsel ifadenin float veri türüne güvenli dönüşümü
        urun_fiyati = float(girdi)
        
        # Hatalı/Mantıksız Veri Girişinin Filtrelenmesi
        if urun_fiyati <= 0:
            print("Hata: Ürün fiyati sifir veya negatif olamaz!")
            print("Bu kararsiz veri listeye eklenmeden atlaniyor...\n")
            # KONTROL İFADESİ: Aşağıdaki satırları çalıştırmadan döngünün başına döner.
            continue
        
        # Geçerli verinin listeye eklenmesi
        sepet_listesi.append(urun_fiyati)
        print(f"{urun_fiyati:.2f} TL sepete eklendi. (Güncel Ürün Adedi: {len(sepet_listesi)})\n")

# 3. AŞAMA: Listenin Döngü Yardımıyla Taranması ve Analiz Edilmesi (for)
print("\n=== FATURA DETAY RAPORU ===")
toplam_tutar = 0
urun_sayaci = 1

for fiyat in sepet_listesi:
    print(f"{urun_sayaci}. Ürün Bedeli: {fiyat:.2f} TL")
    toplam_tutar += fiyat
    urun_sayaci += 1

print("------------------------")
print(f"Sepetteki Toplam Ürün: {len(sepet_listesi)} Adet")
print(f"Net Ödenecek Tutar: {toplam_tutar:.2f} TL")
print("============================")



