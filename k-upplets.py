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



def allelements(tab): 
    elem = tab[0]
    if len(tab)==1:
        return elem+", _"
    del(tab[0])
    for i in tab:
        return elem +"("+ allelements(tab)+")" + ", _" +"("+ allelements(tab)+")"

#for i in range(0,2**len(t)): print([t[j] for j in range(len(t)) if i//(j+1)%2])
def allelements2(tab): 
    for i in range(0,2**len(tab)): print([tab[j] for j in range(len(tab)) if i//(j+1)%2])


'''
Initialisation(G,sdeb)
1 pour chaque point s de G faire
2    d[s] := infini             /* on initialise les sommets autres que sdeb à infini */3
3 fin pour
4 d[sdeb] := 0                        /* sdeb étant le point le plus proche de sdeb */

Trouve_min(Q)
1 mini := infini
2 sommet := -1
3 pour chaque sommet s de Q
4    si d[s] < mini
5    alors 
6        mini := d[s]
7        sommet := s
8 renvoyer sommet

maj_distances(s1,s2)
1 si d[s2] > d[s1] + Poids(s1,s2)      /* Si la distance de sdeb à s2 est plus grande que */
2                                      /* celle de sdeb à S1 plus celle de S1 à S2 */
3    alors 
4        d[s2] := d[s1] + Poids(s1,s2) /* On prend ce nouveau chemin qui est plus court */
5        prédécesseur[s2] := s1        /* En notant par où on passe */

#Fonction principale
Dijkstra(G,Poids,sdeb)
1 Initialisation(G,sdeb)
2 Q := ensemble de tous les nœuds
3 tant que Q n'est pas un ensemble vide faire
4       s1 := Trouve_min(Q)
5       Q := Q privé de s1
6       pour chaque nœud s2 voisin de s1 faire
7           maj_distances(s1,s2)
8       fin pour
9 fin tant que

1 A = suite vide
2 s := sfin
3 tant que s != sdeb faire
4   A = A + s                 /* on ajoute s à la suite A */
5   s = prédécesseur[s]       /* on continue de suivre le chemin */
6 fin tant que
'''
