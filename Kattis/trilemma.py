import math

def dist(pA,pB):
    result = math.sqrt((pA["x"]-pB["x"])**2+(pA["y"]-pB["y"])**2)
    return round(result,10)

def cos(os,as1,as2):
    #os : opposite side, as: adjacent side
    result = (as1**2+as2**2-os**2)/(2*as1*as2)
    return round(result,10)

def are_colinears(angles_cosinus):
    return any([(cos in [-1,1]) for cos in angles_cosinus])

n = int(input())
for i in range(n):
    
    triangle_classification = "acute"
    is_isosceles = True
    is_triangle = True
    
    x1,y1,x2,y2,x3,y3 = map(int,input().split(" "))
    p1, p2, p3 = {"x":x1,"y":y1}, {"x":x2,"y":y2}, {"x":x3,"y":y3}
    a, b, c = dist(p2,p3), dist(p1,p3), dist(p1,p2)
    coss = list()
    try:
        coss = [cos(a,b,c), cos(b,a,c), cos(c,a,b)]
    except ZeroDivisionError:
        is_triangle = False
    else:
        is_triangle = not are_colinears(coss)
    result = ""
    if is_triangle:
        is_isosceles = a==b or a==c or b==c
        for cos_val in coss:
            if cos_val==0:
                triangle_classification = "right"
                break
            elif cos_val<0:
                triangle_classification = "obtuse"
                break
        if is_isosceles: result+="isosceles "
        else: result+="scalene "
        result+=triangle_classification+" triangle"
    else:
        result = "not a triangle"
    print("Case #{}: {}".format(i+1,result))