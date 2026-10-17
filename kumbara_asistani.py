tl_miktari_metin = input("Kumbaraya atilan TL miktarini giriniz: ")
doviz_kuru_metin = input("Güncel döviz kurunu giriniz: ")

tl_miktari = float(tl_miktari_metin)
doviz_kuru = float(doviz_kuru_metin)

doviz_karsiligi = tl_miktari / doviz_kuru

print(f"Kumbaraya atilan {tl_miktari:.2f} TL tutarinin döviz karşiliği: {doviz_karsiligi:.2f}")

