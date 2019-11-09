import sys

def countVowels(w):
    count=0 
    vowels =['a','e','i','o','u']
    for i in w :
        if i in vowels:
            count=count+1
    return count

def findLargestVowelWords(lines):
    large=0
    result_words=[]
    for line in lines:
        words=line.split(' ')
        for w in words:
            count=countVowels(w)
            if count > large :
                large = count
                del result_words[:]
                result_words.append(w)
            elif count == large :
                result_words.append(w)
    return (result_words,large)

def displayResult(result_array,large):

    for i in result_array:
        new_word=[]
        for j in i:
            if j.isalpha() :
                new_word.append(j)
            
        print('{} {}'.format(large,''.join(new_word)))

def readInputFile():
    try :
        file_handler = open(sys.argv[1])
        lines=file_handler.readlines()
        result_array,large=findLargestVowelWords(lines)
        displayResult(result_array,large)
        file_handler.close()
    except:
        print('No file exist')

readInputFile()