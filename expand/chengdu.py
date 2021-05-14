import os
import re
import codecs
r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
with codecs.open('text.txt', 'r', 'utf8') as file_object:
    lines = file_object.readlines()

    print(lines)
allLine = '{\n"list":\n'+'[\n'
for index in range(len(lines)):
    line = lines[index]
    newLine = ''.join(line.split())
    newLine = newLine.encode(encoding='utf8')
    names = re.sub(r1,'',newLine[12:].decode(encoding="utf8"))
    print(names)
    newLine = '{"code" : "' \
              + newLine[0:12].decode() \
              + '",' \
              + '"text" : "' + names
    if index != len(lines) - 1:
        newLine += '"},\n'
    else:
        newLine += '"}\n'
    allLine += newLine
    print(newLine)
allLine += ']\n' + '}'
filename = './chengdu.json'
with open(filename, 'w',encoding='utf-8') as file_object:
    file_object.write(allLine)