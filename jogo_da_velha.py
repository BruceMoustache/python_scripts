import random

line = '+'.join(['---']*3)
LINE_SPACED = '\n' + line + '\n'
BLANK = ' '
LETERS = list('xo')

def buildGameLine(elements):
    blocks = [ element.center(3) for element in elements ]
    return '|'.join(blocks)

gameSets = [ [BLANK]*3 ] * 3

def buildTicTacToe(grid):
    global LINE_SPACED
    gameLines = [ buildGameLine(line) for line in grid ]
    return LINE_SPACED.join(gameLines)

def randomLeter():
    global LETERS
    return random.choices(LETERS)

def randomLine(num=3):
    return [ randomLeter() for count in range(num) ]

def randomGrid(num=3):
    return [ randomLine() for count in range(num) ]

print( randomLeter() )
print( randomLine() )
test = randomGrid()
print(test)
#print( buildTicTacToe(test) )

