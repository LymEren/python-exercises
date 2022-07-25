# Workshop 1 

# Salary Hike 

# Salary tam sayı veri tipinde maaşınızı temsil eden değerdir. 
# Hike tam sayı veri tipinde maaşınıza yapılacak olan yüzdelik % bazında zam miktarıdır. (bu değerleri kullanıcıdan alınız.)
# Zammın uygulanması sonucu yeni maaşı ekrana yazdırınız.


# ****************************

# Is Prime?

# `num`  bir pozitif tam sayıdır (integer). `num` sayısı eğer bir asal sayı ise `true` döndürün,
#  değilse `false` döndürün. (num değerini kullanıcıdan alınız)

# ****************************


# Salary Hike - Eyyub Eren

print("\n** Salary Hike Ornegi **")

mySalary = int(input("\nLutfen aldiginiz maasi giriniz: "))
hikeRate = int(input("\nYuzde kac zam istersiniz: "))
print(f"Yeni maasiniz: {mySalary + ((mySalary * hikeRate) / 100)} olmustur.")


# Prime Number

print("\n** Prime Number Ornegi **")

myNum = int(input("\nLutfen pozitif bir tam sayi giriniz: "))
resultNum = myNum
primeCounter = 0

tryCounter = True; 
while tryCounter: 

    if myNum <= 0:
        myNum = int(input("\nYanlis bir sayi girdiniz. Lutfen pozitif tam sayi giriniz: "))
        resultNum = myNum
        
    else:
        tryCounter = False
        while myNum % 2 == 0 or myNum % 3 == 0 or myNum % 5 == 0:
            if myNum % 2 == 0:
                myNum = myNum / 2
                primeCounter += 1
            elif myNum % 3 == 0:
                myNum = myNum / 3
                primeCounter += 1
            elif myNum % 5 == 0:
                myNum = myNum / 5
                primeCounter += 1

        # Bu sart olmazsa 22 33 gibi sayilar asal sayi cikiyor
        if myNum > 1:
            primeCounter += 1

        if resultNum == 1:
            print("1 sayısı günümüzde ne asal ne de bileşik kabul edilir ve özel bir durumu vardır. ")

        elif primeCounter > 1 :
            print(f"\n{resultNum} sayisi bir asal sayi degildir.")
        
        else:
            print(f"\n{resultNum} sayisi bir asal sayidir.")
