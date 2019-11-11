import sys
def initialize():
    rect1_tl_x = int(sys.argv[1])
    rect1_tl_y = int(sys.argv[2])

    rect1_br_x = int(sys.argv[3])
    rect1_br_y = int(sys.argv[4])

    rect2_tl_x = int(sys.argv[5])
    rect2_tl_y = int(sys.argv[6])

    rect2_br_x = int(sys.argv[7])
    rect2_br_y = int(sys.argv[8])

    return rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y

def intersectionCheck(rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y):
    
    x_tl_check = (rect1_tl_x > rect2_tl_x and  rect1_tl_x < rect2_br_x)
    x_br_check = (rect1_br_x > rect2_tl_x and  rect1_br_x < rect2_br_x)
    x_check = x_tl_check or x_br_check

    y_tl_check = (rect1_tl_y > rect2_tl_y and  rect1_tl_y < rect2_br_y)
    y_br_check = (rect1_br_y > rect2_tl_y and  rect1_br_y < rect2_br_y)
    y_check = y_tl_check or y_br_check 
    
    return x_tl_check,x_br_check,x_check,y_tl_check,y_br_check,y_check

def findIntersection(x_tl_check,x_br_check,x_check,y_tl_check,y_br_check,y_check,rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y):
    if(x_tl_check and not x_br_check):
        res_tl_x = rect1_tl_x
        res_br_x = rect2_br_x
    if(x_br_check and not x_tl_check ):
        res_tl_x = rect2_tl_x
        res_br_x = rect1_br_x
    if(x_tl_check and x_br_check):
        res_tl_x = rect1_tl_x
        res_br_x = rect1_br_x
    if(y_tl_check and not y_br_check):
        res_tl_y = rect1_tl_y
        res_br_y = rect2_br_y
    if(y_br_check and not y_tl_check):
        res_tl_y = rect2_tl_y
        res_br_y = rect1_br_y
    if(y_tl_check and y_br_check):
        res_tl_y = rect1_tl_y
        res_br_y = rect1_br_y
    return res_tl_x,res_tl_y,res_br_x,res_br_y

def intersection():

    rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y = initialize()

    x_tl_check,x_br_check,x_check,y_tl_check,y_br_check,y_check = intersectionCheck(rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y)
    
    if( x_check and y_check):

        res_tl_x,res_tl_y,res_br_x,res_br_y=findIntersection(x_tl_check,x_br_check,x_check,y_tl_check,y_br_check,y_check,rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y)
        print('({},{}),({},{})'.format(res_tl_x,res_tl_y,res_br_x,res_br_y))

    else:
        rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y,rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y = initialize()
        x_tl_check,x_br_check,x_check,y_tl_check,y_br_check,y_check = intersectionCheck(rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y)
    
        if( x_check and y_check):
            res_tl_x,res_tl_y,res_br_x,res_br_y=findIntersection(x_tl_check,x_br_check,x_check,y_tl_check,y_br_check,y_check,rect1_tl_x,rect1_tl_y,rect1_br_x,rect1_br_y,rect2_tl_x,rect2_tl_y,rect2_br_x,rect2_br_y)
            print('({},{}),({},{})'.format(res_tl_x,res_tl_y,res_br_x,res_br_y))
        else:
            print('None')



intersection()