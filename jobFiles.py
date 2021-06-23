###here will be some notes about work with files

inputFile = "input.txt"
outputFile = "output.txt"
searchLine = "email"

myfile = open(inputFile,mode="r",encoding="utf-8")
myOutFile = open(outputFile,mode="w", encoding="utf-8")###for append file use mode="a"

for line in myfile:
    if searchLine in line:
        print(line)
        myOutFile.write(line)

myfile.close()
myOutFile.close()