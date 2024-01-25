import sys

print("Program Started")

filePaths = sys.argv[1:]
print("Number of arguments: ",sys.argv)
print("File PAths : ",filePaths)

for filePath in filePaths:
    lines = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        # print(lines)

    with open(filePath, 'w') as file:
        for line in lines:
            file.write(line.replace('\t', '    '))

print("Program Completed")