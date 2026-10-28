def hasar_al(mevcut_can, darbe_gucu, kalkan=0):
    
    # Net hasarı hesapla: darbe gücünden kalkanı düş
    net_hasar = darbe_gucu - kalkan

    # Net hasar negatif olamaz (kalkan darbeden büyükse hasar 0 kabul edilir)
    if net_hasar < 0:
        net_hasar = 0

    # Kalan canı hesapla
    kalan_can = mevcut_can - net_hasar

    # Senaryoya göre uygun mesajı yazdır
    if kalkan > 0:
        print(f"Kahraman darbe aldi! Kalkan darbeyi emdi. Kalan Can: {kalan_can}")
    else:
        print(f"Kahraman darbe aldi! Kalkan yok. Kalan Can: {kalan_can}")

    return kalan_can

# ---------------- Ana Program / Test Senaryoları ----------------
if __name__ == "__main__":
    # 1. Senaryo: Kalkansız - Yalın Hasar
    # Beklenen: "Kahraman darbe aldı! Kalkan yok. Kalan Can: 70"
    hasar_al(100, 30)

    # 2. Senaryo: Kalkan Aktif - Değeri Ezme
    # Beklenen: "Kahraman darbe aldı! Kalkan darbeyi emdi. Kalan Can: 80"
    hasar_al(100, 30, 10)


    