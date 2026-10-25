print("=== KOD-ASISTAN AKTİF ÇALIŞMA ORTAMI BAŞLATILDI ===")

# AKTİF DÖNGÜ MOTORU
# Koşul True olduğu sürece program açıkça çıkış istenene kadar kapanmaz.
while True:
    print("\n--- ANA MENÜ ---")
    print("1 - Sepet ve İndirim Hesaplama Katmani")
    print("2 - Sistem Durum Raporunu Görüntüle")
    print("3 - Güvenli Çikiş")
    print("----------------")
    
    secim = input("Lütfen yapmak istediğiniz işlemin numarasini giriniz (1/2/3): ").strip()


    if secim != "1" and secim != "2" and secim != "3":
        print("\nHatali Seçim! Girdiğiniz değer menü standartlarina uymuyor.")
        print("Lütfen yalnizca 1, 2 veya 3 değerlerinden birini giriniz.")
        continue

    
    # ÇOK KRİTERLİ DALLANMA VE DÖNGÜ KONTROL ALANI
    if secim == "1":
        print("\n[MODÜL TETİKLENDİ: Sepet Hesaplama]")
        tutar = float(input("Sepet tutarini giriniz (TL): "))
        if tutar > 500:
            print(f"%10 İndirim Uygulandi! Ödenecek Tutar: {tutar * 0.90:.2f} TL")
        else:
            print(f"Net Ödenecek Tutar: {tutar:.2f} TL")
    
    elif secim == "2":
        print("\n[MODÜL TETİKLENDİ: Örnek Sistem Durumu Raporu]")
        print("Mevcut Sürüm: Kod-Asistan v0.3")
        print("Bellek Durumu: RAM Kararli | Çekirdek Motor: Aktif")
        print("Depo Entegrasyonu: Bulut Deposu Bağlantisi Hazir.")
    
    elif secim == "3":
        print("\nGüvenli çikiş protokolü devreye girdi.")
        print("Güvenli günler dileriz!")
        # KONTROL İFADESİ: Döngü burada tamamen kırılır ve program sonlanır.
        break

print("\n=== PROGRAM BAŞARIYLA KAPATILDI ===")



