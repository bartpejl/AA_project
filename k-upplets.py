from PIL.Image import *

#creer et retourne la liste de tout les couples de points de la carte fournie
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

# la retourne la liste des points de la carte
def allpointsofthemap(map):
    length= map.width
    height = map.height
    list= []
    if(length == 0 or height == 0):
        return list
    for x in range (length):
        for y in range (height):
            list= list + [(x,y)]
    
    return list


#retourne toute les combianisons (en liste)
def allcombinations(tab):
    n=2**len(tab)
    list=[0]*n
    for i in range (2**len(tab)):
        list[i]=([tab[j] for j in range(len(tab)) if i//(j+1)%2])
        #print([tab[j] for j in range(len(tab)) if i//(j+1)%2])
    return list

#algo Dijkstra ---pas fini

def dijkstra(graph, vsource, v):
    dist=[-1]*v # -1 est l infini
    prev=[-1]*v # pas encore de predecesseur
    unusedvertex=v # les sommets du graph
    dist[vsource] = 0
    while (unusedvertex==[]):
        
    
