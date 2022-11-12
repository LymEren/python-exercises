# Sorting by key and value

sortNum = {
    3: 20,
    'veli': 'kelime',
    22: 7,
    'c22': 44,
    -15: 9,
    12: 'eyup',
    11: -5
}

print('Original Dictionary: {}\n'.format(sortNum))

keyList = []
valueList = []
for value in range(len(sortNum)):
    ramOne = list(sortNum.keys())[value]
    keyList.append(ramOne)
    valueList.append(sortNum[ramOne])

# SORTING BY KEY

# Small to Big
keySmall = {}
for valOne in range(len(keyList)):
    for valTwo in range(len(keyList) - valOne - 1):
        if type(keyList[valTwo]) == str or type(keyList[valTwo+1]) == str:
            if str(keyList[valTwo]) > str(keyList[valTwo + 1]):
                keyList[valTwo], keyList[valTwo + 1] = keyList[valTwo + 1], keyList[valTwo]
        else:
            if keyList[valTwo] > keyList[valTwo+1]:
                keyList[valTwo], keyList[valTwo+1] = keyList[valTwo+1], keyList[valTwo]
for valOne in range(len(keyList)):
    keySmall[keyList[valOne]] = sortNum[keyList[valOne]]
print(f"Key -> Small to big: {keySmall}")

# Big to Small
keyBig = {}
for valOne in range(len(keyList)):
    for valTwo in range(len(keyList) - valOne - 1):
        if type(keyList[valTwo]) == str or type(keyList[valTwo + 1]) == str:
            if str(keyList[valTwo]) < str(keyList[valTwo + 1]):
                keyList[valTwo + 1], keyList[valTwo] = keyList[valTwo], keyList[valTwo + 1]
        else:
            if keyList[valTwo] < keyList[valTwo + 1]:
                keyList[valTwo + 1], keyList[valTwo] = keyList[valTwo], keyList[valTwo + 1]
for valOne in range(len(keyList)):
    keyBig[keyList[valOne]] = sortNum[keyList[valOne]]
print(f"Key -> Big to small: {keyBig}\n")


# SORTING BY VALUE

# Small to Big
valueSmall = {}
for valOne in range(len(valueList)):
    for valTwo in range(len(valueList) - valOne - 1):
        if type(valueList[valTwo]) == str or type(valueList[valTwo+1]) == str:
            if str(valueList[valTwo]) > str(valueList[valTwo + 1]):
                valueList[valTwo], valueList[valTwo + 1] = valueList[valTwo + 1], valueList[valTwo]
        else:
            if valueList[valTwo] > valueList[valTwo+1]:
                valueList[valTwo], valueList[valTwo+1] = valueList[valTwo+1], valueList[valTwo]
for valOne in range(len(valueList)):
    keyIndex = list(sortNum.keys())[list(sortNum.values()).index(valueList[valOne])]
    valueSmall[keyIndex] = valueList[valOne]
print(f"Value -> Small to big: {valueSmall}")


# Big to Small
valueBig = {}
for valOne in range(len(valueList)):
    for valTwo in range(len(valueList) - valOne - 1):
        if type(valueList[valTwo]) == str or type(valueList[valTwo + 1]) == str:
            if str(valueList[valTwo]) < str(valueList[valTwo + 1]):
                valueList[valTwo + 1], valueList[valTwo] = valueList[valTwo], valueList[valTwo + 1]
        else:
            if valueList[valTwo] < valueList[valTwo + 1]:
                valueList[valTwo + 1], valueList[valTwo] = valueList[valTwo], valueList[valTwo + 1]
for valOne in range(len(valueList)):
    keyIndex = list(sortNum.keys())[list(sortNum.values()).index(valueList[valOne])]
    valueBig[keyIndex] = valueList[valOne]
print(f"Value -> Big to small: {valueBig}")

# Changing Key - Value
changeKey = []
changeValue = []
for _ in range(len(sortNum)):
    ramOne = list(sortNum.keys())[0]
    changeKey.append(ramOne)
    ramTwo = sortNum[ramOne]
    changeValue.append(ramTwo)
    # Change process started. Value is now key.
    sortNum[ramTwo] = sortNum.pop(ramOne)
    # Key is now value.
    sortNum[ramTwo] = ramOne

print("\nChanging Key - Value", sortNum)
