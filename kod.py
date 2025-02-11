def hesap_programi():
    print("Gelir bilgilerini girin (gelir ve tekrar sayısını virgülle ayırın), 'end' yazarak işlemi bitirin:")
    gelir_listesi = []

    while True:
        veri = input("Gelir girin (örn: 5000, 2) veya 'end': ")
        if veri.lower() == "end":
            break

        try:
            gelir, tekrar = veri.split(",")
            gelir = float(gelir.strip())
            tekrar = int(tekrar.strip())
            gelir_listesi.append(gelir * tekrar)
        except ValueError:
            print("Geçersiz format! Lütfen 'gelir, tekrar' formatında girin. Örneğin: 5000, 2")

    aylik_toplam_gelir = sum(gelir_listesi)
    print(f"\nToplam Aylık Kazancınız: {aylik_toplam_gelir:.2f} TL")

# Programı çalıştırmak için:
hesap_programi()