from random import shuffle

def shuffleOrdinaryArray(arrayRange):
    array = list(arrayRange)
    shuffle(array)
    return array

if __name__ == '__main__':
    rangeObjectString = input()
    arrayRange = eval('range(%s)' % rangeObjectString)
    result = shuffleOrdinaryArray(arrayRange)
    print(result)

# TODO make the shuffleOrdinaryArray function act more userly
# for example:
# >>> 1, 10
# make a list begining in 1 and ending in 9

