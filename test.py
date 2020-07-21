a = [100, 100, 5, 5]
b = [13, 13, 5, 5]


def is_cross(a,b):
    ax1,ay1,ax2,ay2 = a[0],a[1],a[2],a[3]       
    bx1, by1, bx2, by2 = b[0], b[1], b[2], b[3]   

    xA = [ax1,ax2]  
    xB = [bx1,bx2]  

    yA = [ay1, ay2]  
    yB = [by1, by2]  
    print('1')
    if max(xA)<min(xB) or min(xA) > max(xB) or max(yA) < min(yB) or min(yA) > max(yB):
        print('2')
        return False    
    elif max(xA)>min(xB) and min(xA)<min(xB):
        dx = max(xA)-min(xB)
        print('3')
        return True   
    else:
        print('4')
        return True   

print(is_cross(a,b))