import os

fonts = os.listdir('/usr/share/figlet')
for i in range(len(fonts)):
    fonts[i] = fonts[i][:-4]
    print(fonts[i])

testString = 'Hello World'
for font in fonts:
    os.system('figlet -f %s %s' % (font, testString))

