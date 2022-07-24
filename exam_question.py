# Not Kayit/Sonuc Ornegi 3. Gun Odevi - Eyyub Eren

versionNotes = input("\nSinav Defterine Hosgeldiniz!\n\nVersiyon notlarini gormek icin v'ye basiniz. Devam etmek icin bir tusa basin: ")
if versionNotes == "v":
    print("\nSinav Defteri Version 0.2\n- Try-Except dongusu degistirildi.\n- Versiyon kontrol ekrani eklendi.\n- Calisma performansi arttirildi (Yani sanirim)\n")

numExam = input("Eklemek istediginiz ders sayisini giriniz: ")

# Tam sayi girilmesi icin kosul ekledim

# Try Except dongusu version 0.2 de degistirildi.
# while type(numExam) != int:
#     try:
#         int(numExam)
#         numExam = int(numExam)
#     except ValueError:
#         numExam = input("Lutfen tam sayi giriniz. Cikmak icin e'ye basabilirsiniz: ")
#         if numExam == "e":
#             exit()

numSwitch = True # While dongusu icin

while numSwitch:
    if numExam.isnumeric():
        numExam = int(numExam)
        if numExam > 0:
            numSwitch = False
        else:
            numExam = input("Lutfen 0'dan buyuk tamsayi giriniz: ")
    else:
        numExam = input("Lutfen 0'dan buyuk tamsayi giriniz. Cikmak isterseniz 'e' ye basiniz: ")
        if numExam == "e":
            print("\nGorusmek Uzere!")
            exit()
numSwitch = True

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
        
        numSwitch = True
        while numSwitch:
            if selected.isnumeric():
                selected = int(selected)
                if selected > 0:
                    numSwitch = False
                else:
                    selected = input("Lutfen 0'dan buyuk tamsayi giriniz: ")
            else:
                selected = input("Lutfen 0'dan buyuk tamsayi giriniz. Cikmak isterseniz 'e' ye basiniz: ")
                if selected == "e":
                    print("\nGorusmek Uzere!")
                    exit()
        numSwitch = True
        
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
        else:
            print("\nYanlis bir sayi girdiniz. Girdiginiz sinav sayisindan fazla veya az sayi giremezsiniz.")
    
    elif (detail == "h"):
        askRetry = False
        print("\nGorusmek Uzere!")
        
    else:
        detail = input("\nYanlis bir tusa bastiniz. Lutfen sorgulama icin 'e', programdan cikmak icin 'h'ye basiniz:" )
        # Burada tekrar input almazsam detail 'e' veya 'h'den farkli bir input aldigi icind loop'a giriyor.


# Incelediginiz icin tesekkurler :) Github: https://github.com/LymEren
