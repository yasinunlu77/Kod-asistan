DOSYA_ADI = "geri_bildirimler.txt"

print("=== KULLANICI GERİ BİLDİRİM ARŞİVİ ===\n")

print("--- KAYITLI GERİ BİLDİRİMLER ---")
try:
    # Okuma işlemi try bloğu içinde: dosya yoksa program çökmez
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        # readlines() ile tüm satırları listeye al
        satirlar = dosya.readlines()

        # Sayaç yardımıyla numaralandırılmış biçimde listeleme
        sayac = 1
        for satir in satirlar:
            # Satır sonundaki '\n' karakterini temizleyerek yazdır
            print(f"{sayac}. Yorum: {satir.strip()}")
            sayac += 1

except FileNotFoundError:
    print("Sistemde kayitli geri bildirim bulunmamaktadir.")

# KULLANICIDAN GERİ BİLDİRİM ALMA
print("\n--- YENİ GERİ BİLDİRİM EKLE ---")
yeni_yorum = input("Asistan hakkindaki geri bildiriminizi yaziniz: ")

# ARŞİVLEME — 'a' (append) modu ile dosyaya ekleme
with open(DOSYA_ADI, "a", encoding="utf-8") as dosya:
    # Alt satıra geçme komutu (\n) ile birlikte yaz
    dosya.write("\n" + yeni_yorum)

print("\n[BİLGİ] Geri bildiriminiz arşive kalici olarak kaydedildi.")
print(f"[BİLGİ] Dosya konumu: {DOSYA_ADI}")


