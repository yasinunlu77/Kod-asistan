print("=== KOD-ASİSTAN SİSTEMİNE HOŞ GELDİNİZ ===")
kullanici_adi = input("Lütfen adinizi giriniz: ")
print(f"Merhaba {kullanici_adi}. Giriş başarili. Lütfen yapmak istediğiniz işlemi seçiniz:\n")

# Menü Standartlarının Sunulması
print("1 - Siber Güvenlik ve Kimlik Doğrulama Testi")
print("2 - Kararli Vücut Kitle İndeksi Hesaplayici")
print("3 - Sistem Sürüm Bilgisi ve Çikiş")

secim = input("\nSeçiminiz (1/2/3): ")

if secim == "1":
    print("\n[SİBER GÜVENLİK MODÜLÜ AKTİF]")
    Kullanici_turu = input("Kullanici türünüzü giriniz (Yönetici/Misafir): ")
    if Kullanici_turu == "Yönetici":
        print("Tam yetki sağlandi. Tüm kaynak kodlar erişime açik.")
    elif Kullanici_turu == "Misafir":
        print("Kisitli yetki sağlandi. Sadece okuma modundasiniz.")
    else:
        print("Tanimsiz Rol! Güvenlik protokolü devreye girdi.")

elif secim == "2":
    print("\n[VÜCUT KİTLE İNDEKSİ HESAPLAYICI AKTİF]")
    kilo = float(input("Kilonuzu giriniz (kg): "))
    boy = float(input("Boyunuzu giriniz (Örn: 1.75): "))
    vki = kilo / (boy ** 2)
    
    # f-string ile biçimlendirilmiş çıktı
    print(f"\nHesaplanan İndeks Değeriniz: {vki:.2f}")
    
    # VKI Sonucunu Çok Kriterli Değerlendirme
    if vki < 18.5:
        print("Durum: Standart değerlerin altindasiniz.")
    elif 18.5 <= vki < 25:
        print("Durum: Tebrikler, standart değerdesiniz.")
    else:
        print("Durum: Standart değerlerin üzerindesiniz.")

elif secim == "3":
    print(f"\nSistemden çikiliyor... Güvenli günler dileriz {kullanici_adi}.")
    print("Mevcut Proje Deposu: GitHub v0.3 - Kararli Sürüm.")

else:
    print("\nHatali Seçim! Lütfen menüde belirtilen rakamlardan (1, 2 veya 3) birini giriniz.")


