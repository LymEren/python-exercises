getInfo = open("studentInfos.txt", "r")
getNote = open("studentsNotes.txt", "r")

with open(r"studentsNotes.txt", 'r') as ln:
    lineCount = len(ln.readlines())

def std_result():
    print("Ogrenci Adi: {}, Sinav sonucu: {}, Harf Notu: {}".format(stdInfo,stdNote,stdResult))
def std_error():
    print("Ogrenci Adi: {}, Lutfen ogrencinin notunu kontrol ediniz. (0 ile 100 arasi olmalidir)".format(stdInfo))

for _ in range(lineCount):
    stdInfo = getInfo.readline().strip()
    stdNote = getNote.readline().strip()

    if stdNote.isnumeric() == True:
        stdResult = int(float(stdNote))
        if stdResult >= 0 and stdResult <= 39:
            stdResult = "E"; std_result()
        elif stdResult >= 40 and stdResult <= 54:
            stdResult = "D"; std_result()
        elif stdResult >= 55 and stdResult <= 69:
            stdResult = "C"; std_result()
        elif stdResult >= 70 and stdResult <= 84:
            stdResult = "B"; std_result()
        elif stdResult >= 85 and stdResult <= 100:
            stdResult = "A"; std_result()
        else:
            std_error()

    else:
        if stdNote == 'Girmedi':
            stdResult = "F"
            std_result()
        else:
            std_error()

