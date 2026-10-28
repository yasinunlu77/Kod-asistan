def net_tutar_hesapla(sepet_tutari, indirim_orani):
    """Gelen verileri işleyip net tutari döndüren modül fonksiyonu"""
    indirim_miktari = sepet_tutari * (indirim_orani / 100)
    return sepet_tutari - indirim_miktari

