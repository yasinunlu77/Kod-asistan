print("=== KOD-ASISTAN: GEÇİCİ BELLEK (RAM) DENETİM PANELİ ===\n")

# KÜRESEL DEĞİŞKENLER (Global Scope)
# Bu değişkenler programın en başında tanımlandığı için tüm fonksiyonlardan okunabilir.
asistan_adi = "KODİ"
sistem_surumu = "v1.2"

def asistan_raporu_bas():
    asistan_adi = "YENİ_KODİ"
    # YEREL DEĞİŞKEN (Local Scope)
    # Bu değişken fonksiyonun içerisinde tanımlanır. 
    # Döndürülen veya başka bir yapı tarafından referans verilen bir nesne içermiyorsa, fonksiyonun görevi bittiğinde belleği temizlenir.
    bellek_durumu = "Kararli / RAM Optimize Edildi"
    
    print("[FONKSİYON İÇİ] Küresel verilere erişiliyor...")
    print(f"Cekirdek Asistan: {asistan_adi} | Sürüm: {sistem_surumu}")
    print(f"Sistem Durumu: {bellek_durumu}\n")
# =====================================================================
# ANA PROGRAM AKIŞI
# =====================================================================
print("[ANAPROGRAM] Fonksiyon çağrisi başlatiliyor...")
asistan_raporu_bas()

print("[ANAPROGRAM] Fonksiyon bitti ve fonksiyonun bellek hücresi temizlendi.")
print("--------------------------------")
print(f"Ana programdan küresel veriye erişim testi: {asistan_adi} -> BAŞARILI")

# BELLEK SINIR İHLALİ TEST ALANI: Aşağıdaki satırın başındaki (#) işaretini kaldırarak hata avcılığı yapınız.
# print(f"Ana programdan yerel veriye erişim testi: {bellek_durumu}")




