# Not Kayit/Sonuc Ornegi - Eyyub Eren


versionNotes = input("\nNot Defterine Hosgeldiniz!\n\nVersiyon notlarini gormek icin v'ye basiniz. Devam etmek icin bir tusa basin: ")
if versionNotes == "v":
    print("\nNot Defteri Version 0.3\n\n- Girdinin numara olup olmadigini kontrol eden dongu fonksiyona cevrildi (tryNum fonksiyonu).\n- Vize ve Final kullacini girislerinde numara yazilmadigi durumda hata duzeltildi.\n- Tum sinav sonuclarini gosterme ozelligi eklendi\n")

numExam = input("\nEklemek istediginiz ders sayisini giriniz: ")


# Tekrarlayan girdi kontrol islemleri icin fonksiyon kullanildi.

def tryNum(x):

    numSwitch = True # While dongusu icin
    while numSwitch:
        if x.isnumeric():
            x = int(x)
            if x >= 0:
                numSwitch = False
                return x
            else:
                x = input("Lutfen 0'dan buyuk tamsayi giriniz: ")
        else:
            x = input("Lutfen 0'dan buyuk tamsayi giriniz. Cikmak isterseniz 'e' ye basiniz: ")
            if x == "e":
                print("\nGorusmek Uzere!")
                exit()
    numSwitch = True

numExam = tryNum(numExam)

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

    midtermExam = input(f"\n{value+1}. dersin vize notunu giriniz: ")
    midtermExam = tryNum(midtermExam) # Yeni fonksiyon (tryNum) kullanildi.
    examList["Vize"].append(midtermExam)

    finalExam = input(f"{value+1}. dersin final notunu giriniz: ")
    finalExam = tryNum(finalExam) # Yeni fonksiyon (tryNum) kullanildi.
    examList["Final"].append(finalExam)

    result = ((midtermExam * 0.4) + (finalExam * 0.6)) # Gecme notunu hesapladik
    examList["Ortalama"].append(result)
    
    if result >= 50:
        examList["Sonuc"].append(f"Gectiniz")
        counter1 += 1
    elif result < 50:
        examList["Sonuc"].append(f"Kaldiniz")
            

print(f"\n*** {numExam} dersten {counter1} tanesini gectiniz! Tebrikler! ***")

############################################################################

# Alt kisimda kullaniciya detaylari gorebilmesi icin bir panel olusturdum.
# Kullanici istedigi sinavi secerek sonuclarina detayli bir sekilde bakabilir.

# detail degiskeni kullanicinin devam etmek isteyip istemedigi inputu sakliyor.
detail = input("\nSonuclarinizi detayli gormek ister misiniz? (Evetse 'e', hayirsa 'h'ye basiniz): ")

askRetry = True # Yeniden sorgulama icin boolean bir degisken kullandim.

while askRetry:

    if (detail == "e"):
        selected = input("\nKacinci sinavin sonucunu gormek istersiniz? (Tum sonuclari gormek icin 0'a basiniz): ") 
        
        selected = tryNum(selected)
        
        if (selected <= numExam and selected >= 1):

            print(f"\n{selected}. Sinavin Sonuclari:\nVize: {examList['Vize'][selected-1]}\nFinal: {examList['Final'][selected-1]}\nOrtalama: {examList['Ortalama'][selected-1]}\nSonuc: {examList['Sonuc'][selected-1]}")
            
            retry = input("\nBaska bir sonuca bakmak ister misiniz? (Evetse 'e', hayirsa 'h'ye basiniz): ")
            if (retry == "e"):
                continue
            elif (retry == "h"):
                askRetry = False
                print("\nGorusmek Uzere!")
            else:
                detail = input("Yanlis bir tusa bastiniz. Lutfen sorgulama icin 'e', programdan cikmak icin 'h'ye basiniz: ")
        elif(selected == 0 ):
            for value in range (numExam):
                print(f"\n{value+1}. Sinavin Sonuclari:\nVize: {examList['Vize'][value]}\nFinal: {examList['Final'][value]}\nOrtalama: {examList['Ortalama'][value]}\nSonuc: {examList['Sonuc'][value]}\n")
                
        else:
            print("\nYanlis bir sayi girdiniz. Girdiginiz sinav sayisindan fazla veya az sayi giremezsiniz.")
    
    elif (detail == "h"):
        askRetry = False
        print("\nGorusmek Uzere!")
        
    else:
        detail = input("\nYanlis bir tusa bastiniz. Lutfen sorgulama icin 'e', programdan cikmak icin 'h'ye basiniz:" )
        # Burada tekrar input almazsam detail 'e' veya 'h'den farkli bir input aldigi icind loop'a giriyor.


# Incelediginiz icin tesekkurler :) Github: https://github.com/LymEren
