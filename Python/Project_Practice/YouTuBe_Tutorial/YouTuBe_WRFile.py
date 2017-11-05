fw = open('sample.txt', 'w')
fw.write('This is a first line\n')
fw.write('This is a second line\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()