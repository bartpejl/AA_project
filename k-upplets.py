from PIL.Image import *

def upplet(map):
    length= map.width
    height = map.height
    list=[]
    if(length == 0 or height == 0):
        return list
    for x1 in range (length):
        for y1 in range (height):
            for x2 in range (length):
                for y2 in range (height):
                    if (x1 != x2 or y1 != y2):
                        list= list + [((x1,y1),(x2,y2))]
    return list
