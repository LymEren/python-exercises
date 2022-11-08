# Calculates the results by taking student information from text file and exam grades from another text file.

getInfo = open("studentInfo.txt", "r")
getNote = open("studentsNotes.txt", "r")

with open(r"studentsNotes.txt", 'r') as ln:
    lineCount = len(ln.readlines())


def std_result():
    result = ("Students Name: {}, Exam Result: {}, Grade: {}\n".format(stdInfo, stdNote, stdResult))
    with open('studentsResult.txt', 'a') as studentWriter:
        studentWriter.write(result)


def std_error():
    result = ("Students Name: {}, Please check the student's grade. (It must be between 0 and 100)\n".format(stdInfo))
    with open('studentsResult.txt', 'a') as studentWriter:
        studentWriter.write(result)

for _ in range(lineCount):
    stdInfo = getInfo.readline().strip()
    stdNote = getNote.readline().strip()

    if stdNote.isnumeric():
        stdResult = int(float(stdNote))
        if 0 <= stdResult <= 39:
            stdResult = "E"
            std_result()
        elif 0 <= stdResult <= 54:
            stdResult = "D"
            std_result()
        elif 55 <= stdResult <= 69:
            stdResult = "C"
            std_result()
        elif 70 <= stdResult <= 84:
            stdResult = "B"
            std_result()
        elif 85 <= stdResult <= 100:
            stdResult = "A"
            std_result()
        else:
            std_error()

    else:
        if stdNote == 'Girmedi':
            stdResult = "F"
            std_result()
        else:
            std_error()
