codeTree = [None, None, 'e', 't', 'i', 'a', 'n', 'm', 's', 'u', 'r', 'w',
            'd', 'k', 'g', 'o', 'h', 'v', 'f', None, 'l', None, 'p',
            'j', 'b', 'x', 'c', 'y', 'z', 'q']
for i in range(100):
    codeTree.append(None)
codeTree[32] = '5'
codeTree[33] = '4'
codeTree[35] = '3'
codeTree[39] = '2'
codeTree[42] = '+'
codeTree[47] = '1'
codeTree[48] = '6'
codeTree[49] = '='
codeTree[50] = '/'
codeTree[56] = '7'
codeTree[60] = '8'
codeTree[62] = '9'
codeTree[63] = '0'

# Dot = left
# Dash = Right

def getChar(morseChar):
    if morseChar == '/':
        return ' '
    index = 1
    for i in range(len(morseChar)):
        index *= 2
        if morseChar[i] == '-':
            index += 1
    return codeTree[index]

file = open(input("file: "), "r")
output = ''
for line in file:
    morseCharList = line.split()
    for morseChar in morseCharList:
        output+=getChar(morseChar)
print(output)
