# Aynı klasördeki asistan_finans.py dosyası projeye dâhil edilir.
import asistan_finans

print("=== KOD-ASİSTAN: ÇOKLU DOSYA VE MODÜLER ALTYAPI MOTORU ===\n")

# Kullanıcı veri girişleri
girdi_sepet = 500.0
girdi_indirim = 10.0

print("[ANAPROGRAM] Harici modüldeki fonksiyon nokta (.) operatörüyle çağriliyor...")

# AD ALANI KONTROLÜ: Fonksiyon çağrılırken hangi modülden geldiği belirtilir.
odenecek_tutar = asistan_finans.net_tutar_hesapla(girdi_sepet, girdi_indirim)

print("--------------------------------")
print(f"Modüler Hesaplama Sonucu Ödenecek Net Tutar: {odenecek_tutar:.2f} TL")
print("===========================================")



