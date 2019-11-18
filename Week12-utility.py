#https://github.com/Uebbels/CSCI102Lab12
#Brendan Uebelhoer
#CSCI 102 – Section C
#Week 12 - Part B

def PrintOutput(input):
    output = 'OUTPUT ' + str(input)
    print(output)

def LoadFile(filename):
    with open(filename,'r') as file:
        contents = file.read()
        lines = contents.split('.')
    return lines

def UpdateString(string,replacement,index):
    output = []
    for i in range(len(string)):
        if i == index:
            output.append(replacement)
        else:output.append(string[i])
    output = ''.join(output)
    return output

def FindWordCount(list,string):
    for i in list:
        j=0
        while j != -1:
            j = i.find(string, j)
            print('debug 1', i.find(string,j))
            if j == -1:
                continue
            elif j != -1:
                counter += 1
                j += 1
    return counter

def ScoreFinder(players,score,target):
    playersLower =[]
    for i in players:
        playersLower.append(i.lower())
    if target.lower() in playersLower:
        index = playersLower.index(target)
        PrintOutput('%s got a score of %d' %(players[index], score[index]))
    else:
        PrintOutput("player not found")

def Union(list1,list2):
    outlist = list1
    for i in list2:
        if i in outlist:
            continue
        else:
            outlist.append(i)
    return outlist

