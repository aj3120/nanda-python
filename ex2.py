import sys

def isWhiteLine(s):
    white_space_remove_flag = True
    s=s.strip('\n')
    for i in s :
        if i != ' ' :
            white_space_remove_flag = False
            break
    if white_space_remove_flag:
        return 'TRUE'
    else:
        return 'FALSE'

try :
    file_handler = open(sys.argv[1])
    while True:
        line=file_handler.readline()
        if not line:
            break
        elif isWhiteLine(line) == 'FALSE':
            print(line,end="")
    print('')
    file_handler.close()
except:
    print('No file exist')
