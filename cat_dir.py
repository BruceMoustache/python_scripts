import os


def header(text, countOfSpaces, completionChar='='):
    headerText = addBorder(text)
    return headerText.center(countOfSpaces, completionChar)

def addBorder(string, borderWidth=1, char=' '):
    border = char * borderWidth
    return border + string + border

def tail(fileInstance):
    countOfLines = len(fileInstance.readlines())
    return f'lines: {countOfLines}'

userPath = input('Diretorio: ')
os.chdir(userPath)
files = os.listdir()
for fileName in files:
    try:
        fileInstance = open(fileName)
        fileContent = fileInstance.read()
        print(header(fileName, 25))
        print(fileContent)
        print(tail(fileInstance))
    except IsADirectoryError:
        continue

