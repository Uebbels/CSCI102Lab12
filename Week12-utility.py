#https://github.com/Uebbels/CSCI102Lab12
#Brendan Uebelhoer
#CSCI 102 – Section C
#Week 12 - Part B

def PrintOutput(input):
    output = 'OUTPUT ' + str(input)
    print(output)

def loadfile(filename):
    with open(filename,'r') as file:
        contents = file.read()
        lines = contents.split('.')
    return lines
print(loadfile('test.txt'))