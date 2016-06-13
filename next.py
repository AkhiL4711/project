BUFFSIZE = 2500
iFileName = "test.txt"
oFileName = "test2.txt"
iFile = open(iFileName, 'r' )
oFile = open(oFileName, 'w' )
buffer = iFile.read( BUFFSIZE )
while( len( buffer )):
    oFile.write(buffer)
    print("{} bytes written to {}".format(len(buffer), oFileName))
    buffer = iFile.read(BUFFSIZE)
print("Done")