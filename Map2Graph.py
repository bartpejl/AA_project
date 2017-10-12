def transform(adjacencelist, listpixel, i, j, imax, jmax, parameter):
    if not(i<=0):
        if listpixel[i-1,j] != black:
            adjacencelist[i+j*imax] = i-1 + j*imax
    if not(i>=imax):
        if listpixel[i+1,j] != black:
            adjacencelist[i+j*imax] = i+1 + j*imax
    if not(j<=0):
        if listpixel[i,j-1] != black:
            adjacencelist[i+j*imax] = i + (j-1)*imax
    if not(j>=jmax):
        if listpixel[i,j+1] != black:
            adjacencelist[i+j*imax] = i + (j+1)*imax
    if parameter != "NoDiagonals" :#si on concidere les diagonales    
        if not(i<=0 or j<=0):
            if listpixel[i-1,j-1] != black:
                adjacencelist[i+j*imax] = i-1 + (j-1)*imax
        if not(i>=imax or j<=0):
            if listpixel[i+1,j-1] != black:
                adjacencelist[i+j*imax] = i+1 + (j-1)*imax
        if not(i<=0 or j>=jmax):
            if listpixel[i,j-1] != black:
                adjacencelist[i+j*imax] = i-1 + (j+1)*imax
        if not(i>=imax or j>=jmax):
            if listpixel[i,j+1] != black:
                adjacencelist[i+j*imax] = i+1 + (j+1)*imax

def map2graph (listpixel, imax ,jmax, parameter):
    #creation d'une liste d adjacence
    adjacencelist = []
    for i in imax:
        for j in jmax:
            if listpixel[i,j] != "black":
                transform(adjacencelist, listpixel, i, j, imax, jmax, parameter)
    return listpixel

