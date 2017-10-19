
#verifie si un ensemble de sommet est dominat, graph est une liste d'adj, vertices une liste de sommet
def checkdominance(graph,vertices):
    dominatedset =[]
    numbertodom= 0 #nombre de sommets à dominer
    for s in graph:
        dominatedset+=0 # liste initialisee à 0
        numbertodom += 1 # on incremente le nb de sommet à dominer 
    for d in vertices:
        dominatedset[d] = 1 # sommet marqué
        #marquer les sommets adjacents
            
