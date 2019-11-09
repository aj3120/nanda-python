def isListOfInts(list_numbers):
    int_flag = True
    for i in list_numbers :
        if type(i) is not int:
            int_flag = False
            break
    return int_flag

def testList(list_numbers):
    if type(list_numbers) is list:
        print(isListOfInts(list_numbers))
    else:
        print('Value Error : {} arg not of <list> type'.format(list_numbers))


testList([])