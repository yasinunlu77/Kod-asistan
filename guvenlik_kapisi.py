
# Kullanıcıdan SADECE rol bilgisini al
rol_girdi = input("Lütfen rolünüzü giriniz (yönetici / personel): ")

# Rol bilgisinin küçük harfe dönüştürülmüş hâlini bir değişkene ata
rol = rol_girdi.strip().lower()

# if-elif-else merdiveni
if rol == "yönetici":
    # Yönetici: güvenlik derecesi HİÇ SORULMAZ
    print("Erişim izni verildi. Hoş Geldiniz Sayin Yönetici.")

elif rol == "personel":
    # Personel: SADECE burada güvenlik derecesi sorulur
    guvenlik_derecesi = int(input("Lütfen güvenlik derecenizi giriniz (1-5): "))

    # İç içe (nested) kontrol
    if guvenlik_derecesi >= 3:
        print("Erişim izni verildi. Laboratuvar alanina geçebilirsiniz.")
    else:
        print("Erişim engellendi. Yetersiz güvenlik derecesi!")

else:
    # Geçersiz rol: güvenlik derecesi HİÇ SORULMAZ
    print("Hatali rol tanimlamasi! Güvenlik protokolü devreye girdi.")



