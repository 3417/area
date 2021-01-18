import os
import codecs

with codecs.open('area.txt', 'r', 'utf8') as file_object:
    lines = file_object.readlines()
allLine = '{\n"list":\n'+'[\n'
for index in range(len(lines)):
    line = lines[index]
    newLine = ''.join(line.split())
    newLine = newLine.encode(encoding='utf8')
    names = newLine[6:].decode(encoding="utf8")
    newLine = '{"code" : "' \
              + newLine[0:6].decode() \
              + '",' \
              + '"name" : "' + names
    if index != len(lines) - 1:
        newLine += '"},\n'
    else:
        newLine += '"}\n'
    allLine += newLine
    print(newLine)
allLine += ']\n' + '}'
filename = './output.json'
with open(filename, 'w',encoding='utf-8') as file_object:
    file_object.write(allLine)