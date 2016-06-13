iFile = open('test.txt', 'r')
oFile = open('test2.txt', 'w')
for line in iFile:
    oFile.write(line)
print('Done')