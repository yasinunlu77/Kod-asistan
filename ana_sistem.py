# ana_sistem.py
# Ana sistem dosyası: yardımcı modülü alias ile içe aktarır

import guvenlik_araclari as ga  # 'ga' kısa takma adıyla modülü içe aktardık

# Fonksiyonu alias + nokta operatörüyle çağırıyoruz
parola = ga.parola_uret()
print("Üretilen geçici parola:", parola)

# Modül içindeki YEREL değişkene dışarıdan erişmeyi deniyoruz.
# Bu satır AttributeError fırlatacaktır çünkü gecici_parola modülün
# global alanında değil, fonksiyonun yerel kapsamında tanımlıdır.
# print(ga.gecici_parola) 