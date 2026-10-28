import random

print("=== KOD-ASISTAN: SAYI TAHMİN OYUNU MODÜLÜ AKTİF ===")
print("Sistem 1 ile 50 arasinda gizli bir sayi belirledi. Bulmak için 5 hakkiniz var!\n")

# 1. AŞAMA: Oyun parametrelerinin ve gizli sayının bellekte hazırlanması
gizli_sayi = random.randint(1, 50)
kalan_hak = 5
tahmin_sayaci = 0

# 2. AŞAMA: Oyun Döngüsünün Başlatılması
while kalan_hak > 0:
    girdi = input(f"Kalan Hakkiniz ({kalan_hak}). Tahmininizi giriniz: ").strip()
    tahmin = int(girdi)
    
    # GEÇERSİZ ARALIK GİRİŞİNİN "CONTINUE" İLE ATLANMASI
    if tahmin < 1 or tahmin > 50:
        print("Uyari: Tahmininiz 1 ile 50 arasinda olmalidir!")
        print("Sistem kararliliğini korumak için bu adim atlaniyor ve hakkiniz eksilmiyor.\n")
        # KONTROL İFADESİ: Aşağıdaki kodları çalıştırmadan doğrudan döngü koşuluna döner.
        continue
    
    # Geçerli bir tahmin yapıldığı için sayaçları güncelleme adımı
    tahmin_sayaci += 1
    kalan_hak -= 1
    
    # 3. AŞAMA: ÇOK KRİTERLİ DOĞRULAMA VE DÖNGÜ YÖNETİMİ
    if tahmin == gizli_sayi:
        print(f"\nTebrikler! Gizli sayiyi {tahmin_sayaci}. denemenizde buldunuz.")
        # KONTROL İFADESİ: Koşulun hâlâ hakkı olmasına bakılmaksızın döngüyü anında kırar.
        break
    elif tahmin > gizli_sayi:
        print("İpucu: Daha KÜÇÜK bir sayi girmelisiniz.\n")
    else:
        print("İpucu: Daha BÜYÜK bir sayi girmelisiniz.\n")

# 4. AŞAMA: Oyun Sonu Durum Kontrolü
if kalan_hak == 0 and tahmin != gizli_sayi:
    print("\nMaalesef tahmin hakkiniz bitti ve oyun sonlandi.")
    print(f"Sistemin belirlediği gizli sayi: {gizli_sayi} idi. Bir sonraki sefere başarilar!")

print("\n== OYUN MODÜLÜ KAPATILDI ===")





