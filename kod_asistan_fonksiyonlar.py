# 1. AŞAMA: MODÜLER FONKSİYON TANIMLARI
def karsilama_modulu(ad, rol):
    """Kullaniciya özel bir selamlama metni oluşturur ve döndürür."""
    mesaj = f"Sayin {ad}, '{rol}' yetkisiyle sisteme hoş geldiniz."
    return mesaj

def yas_hesapla(dogum_yili, mevcut_yil):
    """Yaklaşik yaşi hesaplayip döndürür."""
    yas = mevcut_yil - dogum_yili
    return yas

# 2. AŞAMA: ANA AKIŞ
print("=== KOD-ASİSTAN MODÜLER PANEL ===")

# Dinamik veri girişleri
ad = input("Adinizi giriniz: ")
rol = input("Rolünüzü giriniz (Yönetici/Misafir): ")
dogum_yili = int(input("Doğum yilinizi giriniz: "))
mevcut_yil = 2026

# Fonksiyonların çağrılması ve return edilen değerlerin değişkenlere atanması
karsilama_metni = karsilama_modulu(ad, rol)
hesaplanan_yas = yas_hesapla(dogum_yili, mevcut_yil)

# Sonuçların ekrana yazdırılması
print("\n--- SİSTEM RAPORU ---")
print(karsilama_metni)
print(f"Yaklaşik yaşiniz: {hesaplanan_yas}")



