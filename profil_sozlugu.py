kullanici_profili = {}

kullanici_profili["Kullanici_1"] = {
    "ad": "Ahmet",
    "dil": "Türkçe",
    "tema": "Açik"
}

# Başlangıç durumunu görelim
print("Başlangiç profili:", kullanici_profili["Kullanici_1"])

# Tema tercihini doğrudan atama operatörüyle "Koyu" olarak güncelliyoruz
kullanici_profili["Kullanici_1"]["tema"] = "Koyu"
print("Tema güncellendi ->", kullanici_profili["Kullanici_1"]["tema"])

# Sistemde var olmayan "bildirim_sesi" anahtarını .get() ile güvenli sorguluyoruz
bildirim_ayari = kullanici_profili["Kullanici_1"].get("bildirim_sesi")

print("Bildirim sesi ayari:", bildirim_ayari)  # None döner, KeyError fırlatmaz

# Güncel profilin tamamını gösterelim
print("Güncel profil:", kullanici_profili["Kullanici_1"])

