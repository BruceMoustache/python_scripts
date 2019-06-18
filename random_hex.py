from random import randint

def hexToDec(hexNumber):
    pass

def decToHex(decNumber):
    pass

def randomHexInInterval(lower, higher):
    number = randint(lower, higher)
    hexNumber = hex(number)[2:].upper()
    return hexNumber

def randomHexWithDigits(digitsCount):
    lower = 16 ** digitsCount
    higher = 16 ** (digitsCount + 1) - 1
    return randomHexInInterval(lower, higher)

if __name__ == '__main__':
    digitsCount = int(input('Digits count: '))
    print( randomHexWithDigits(digitsCount) )

