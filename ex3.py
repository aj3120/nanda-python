def isListOfInts(list_numbers):
    if type(list_numbers) is list:
        int_flag = True
        for i in list_numbers :
            if type(i) is not int:
                int_flag = False
                break
        return int_flag
    else:
        raise ValueError('{} arg not of <list> type'.format(list_numbers))

def testList(list_numbers):
    result = isListOfInts(list_numbers)
    if(result==True or result == False):
        print('{} --> {}'.format(list_numbers,result))
        


testList([1,5,7])
