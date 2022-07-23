# Not Kayit/Sonuc Ornegi 3. Gun Odevi - Eyyub Eren

print("Sinav Defteri version 00000000000.1\n\nHosgeldiniz!")

numExam = input("Eklemek istediginiz ders sayisini giriniz: ")

# Tam sayi girilmesi icin kosul ekledim

while type(numExam) != int:
    try:
        int(numExam)
        checkPoint = True
        numExam = int(numExam)
    except ValueError:
        checkPoint = False
        numExam = input("Lutfen tam sayi giriniz. Cikmak icin e'ye basabilirsiniz: ")
        if numExam == "e":
            exit()

# Veriler icin dictionary kullandim.
examList = {

    "Vize"     : [],
    "Final"    : [],
    "Ortalama" : [],
    "Sonuc"    : []
}   

counter1 = 0 # Toplam gecilen ders sayaci.

# Kullanici veri girislerini yapiyor.
for value in range(numExam):

    midtermExam = float(input(f"\n{value+1}. dersin vize notunu giriniz: "))
    examList["Vize"].append(midtermExam)

    finalExam = float(input(f"{value+1}. dersin final notunu giriniz: "))
    examList["Final"].append(finalExam)

    result = ((midtermExam * 0.4) + (finalExam * 0.6)) # Gecme notunu hesapladik
    examList["Ortalama"].append(result)
    
    if result >= 50:
        examList["Sonuc"].append(f"Gectiniz")
        counter1 += 1
    elif result < 50:
        examList["Sonuc"].append(f"Kaldiniz")
            

print(f"\n*** {numExam} dersten {counter1} tanesini gectiniz ***")

############################################################################

# Alt kisimda kullaniciya detaylari gorebilmesi icin bir panel olusturdum.
# Kullanici istedigi sinavi secerek sonuclarina detayli bir sekilde bakabilir.

# detail degiskeni kullanicinin devam etmek isteyip istemedigi inputu sakliyor.
detail = input("\nSonuclarinizi detayli gormek ister misiniz? (Evetse 'e', hayirsa 'h'ye basiniz): ")

askRetry = True # Yeniden sorgulama icin boolean bir degisken kullandim.

while askRetry:

    if (detail == "e"):
        selected = input("Kacinci sinavin sonucunu gormek istersiniz: ") 
        
        # Burada birkac farkli deneme yaptim ve en son while ve try except yapilarini kullandim.
    
        while type(selected) != int: 
            try:
                int(selected)
                checkPoint = True
                selected = int(selected)
            except ValueError:
                checkPoint = False
                selected = input("Lutfen tam sayi giriniz. Cikmak icin e'ye basabilirsiniz: ")
                
                if selected == "e":
                    exit()
        
        if (selected <= numExam and selected >= 1):
            # Bunu eklememin sebebi satir 73'te aciklandi.

            print(f"\n{selected}. Sinavin Sonuclari:\nVize: {examList['Vize'][selected-1]}\nFinal: {examList['Final'][selected-1]}\nOrtalama: {examList['Ortalama'][selected-1]}\nSonuc: {examList['Sonuc'][selected-1]}")
            
            retry = input("\nBaska bir sonuca bakmak ister misiniz? (Evetse 'e', hayirsa 'h'ye basiniz): ")
            if (retry == "e"):
                continue
            elif (retry == "h"):
                askRetry = False
                print("Gorusmek Uzere!")
            else:
                detail = input("Yanlis bir tusa bastiniz. Lutfen sorgulama icin 'e', programdan cikmak icin 'h'ye basiniz: ")
        else:
            print("\nYanlis bir sayi girdiniz. Girdiginiz sinav sayisindan fazla veya az sayi giremezsiniz.")
            # Kullanici eger 1 ders girip 2. sinav sonucuna bakmak isterse ve hata alip daha sonra
            # 1. sinavi secerse, program "selected" degiskeni integer olmadan print satirina giriyor
            # ve "int ile str arasi islem yapamazsin" diyor. Bu nedenle oraya int donusum satiri ekledim.
    
    elif (detail == "h"):
        askRetry = False
        print("Gorusmek Uzere!")
        
    else:
        detail = input("\nYanlis bir tusa bastiniz. Lutfen sorgulama icin 'e', programdan cikmak icin 'h'ye basiniz:" )
        # Burada tekrar input almazsam detail 'e' veya 'h'den farkli bir input aldigi icind loop'a giriyor.


# Incelediginiz icin tesekkurler :) Github: https://github.com/LymEren
