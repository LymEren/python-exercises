# Sart Bloklari - Eyyub Eren

# ----------------------- Bolum Odevi 1
print("\nBolum Odevi 1")

number1 = 26.4
number2 = 55

if number1>number2:
    print("Buyuk Sayi: " + str(number1))
elif number2>number1:
    print("Buyuk Sayi: " + str(number2))

# Cevap 1: Evet
# Cevap 2: Esit oldugu durumda ekran bos



# ----------------------- Bolum Odevi 2
print("\nBolum Odevi 2")

number1 = 5
number2 = 15
number3 = 77

if number1>number2:
    if number1>number3:
        print("En buyuk sayi: " + str(number1))
        if number3>number2:
            print("En kucuk sayi: " + str(number2))
        else:
            print("En kucuk sayi: " + str(number3))

    elif number3>number1:
        print("En buyuk sayi: " + str(number3))
        print("En kucuk sayi: " + str(number2))


elif number2>number1:
    if number2>number3:
        print("En buyuk sayi: " + str(number2))
        if number3>number1:
            print("En kucuk sayi: " + str(number1))
        else:
            print("En kucuk sayi: " + str(number3))

    elif number3>number2:
        print("En buyuk sayi: " + str(number3))
        print("En kucuk sayi: " + str(number1))

# Cevap: Farkli kombinasyonlarda dogru sonuca ulastim



# ----------------------- Bolum Odevi 3

# Sarta bagli degiskenler: Durum kismindaki yukselis veya dusus simgeleri
# Ust panelde anlik degisimlerle beraber rakamlarin arka planinda olusan anlik renk degisimleri
# Kullanici adi ve giris ekrani (ornegin bos birakildiginda) sistemin hata vermesi 
# Bunun gibi bircok sartli bilesen sitede mevcut
