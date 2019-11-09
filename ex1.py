def ruler():
    x = int(input('Enter a number'))
    for i in range(0,2):
        for j in range(1,x+1):
            if j%10 == 0 and i == 0 :
                print(int(j/10),end=" ")
            elif i == 1:
                print(j%10,end=" ")
            else :
                print(" ",end=" ")
        print('\n')

ruler()