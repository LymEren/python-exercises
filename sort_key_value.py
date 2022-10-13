import copy

sortNum = {
    3 : 20,
    2 : 7,
    6 : 44,
    1 : 3
}
# Key olarak siralama yapmak icin olusturulan dizi
keyList = []
# # Value olarak siralama yapmak icin olusturulan dizi
valueList = []

# copy.deecopy non pointer bir kopyalama
oldList = copy.deepcopy(sortNum)
arrLen = len(sortNum)
# Key Value yerlerini degistirme
for _ in range(arrLen):
    # ram1 = keylerin icerigini ram1 degiskenine aktariyor. Burada surekli sifirinci siradakini almamizin sebebi
    #        pop islemi sonrasi birinci siradaki itemin en sona gitmesinden dolayi
    ram1 = list(sortNum.keys())[0]
    keyList.append(ram1)
    # ram2 = ram1'deki keyin karsiligina gelen value'yi tutan degisken
    ram2 = sortNum[ram1]
    valueList.append(ram2)
    # Value key oldu
    sortNum[ram2] = sortNum.pop(ram1)
    # Key value oldu
    sortNum[ram2] = ram1

print("Eski liste: {}".format(oldList))
print(f"Yeni liste: {sortNum}")


#Sözlüğümüzü değere göre sıralamamızı sağlayan bir sıralama mekanizması.
biggestOld = sorted(oldList.items(), key=lambda  x:x[1], reverse = True)
# List tipinden dictionary tipine geciyoruz
biggestOld= dict(biggestOld)

smallestOld = sorted(oldList.items(), key=lambda x:x[1], reverse = False)
smallestOld = dict(smallestOld)

print(f"\nKey'e gore buyukten kucuge liste: {biggestOld}")
print(f"Key'e gore kucukten buyuge liste: {smallestOld}")

biggestNew = sorted(sortNum.items(), key=lambda  x:x[1], reverse = True)
# List tipinden dictionary tipine geciyoruz
biggestNew= dict(biggestNew)

smallestNew = sorted(sortNum.items(), key=lambda x:x[1], reverse = False)
smallestNew = dict(smallestNew)

print(f"\nValue'ye gore buyukten kucuge liste: {biggestNew}")
print(f"Value'ye gore kucukten buyuge liste: {smallestNew}")
