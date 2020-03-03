import matplotlib.pyplot as plt
from sys import stdin

def matrizmult(m1, m2):
    
    f2 = len(m2)
    c1 = len(m1[0])
    m0="Imposible Multiplicar"
    if f2 == c1:
        f = len(m1)
        c = 1
        m0 = [[0] for x in range(f)]        
        for i in range(0,f):
            for j in range(0,c):
                for k in range(0, len(m2)):
                    m = m1[i][k]* m2[k]
                    n = m0[i][j]
                    m0[i][j] = m+n
    return m0

def accionmatrizvector(m1,v1):
    c = []
    d = []
    for i in range (len(m1)):
        c.append([])
        for j in range (len(m1)):
            c[i].append(m1[i][j]*v1[j])
    for i in range (len(c)):
        d.append(sumavector(c[i]))        
    return d

def sumavector(v1):
    if len(v1) < 2 :
        return v1[0]
    elif len(v1) == 2:
        s = v1[0]+v1[1]
        return s
    else:
        s = v1[0]+v1[1]
        for i in range (2,len(v1)):
            s = s+v1[i]
        return s

def canicas(mat,clicks,startingState):
    mat=clicksMatrix(clicks,mat)
    #print(mat)
    return accionmatrizvector(mat,startingState)

def clicksMatrix(clicks,mat):
    for i in range(clicks-1):
        mat=matrizmult(mat, mat)
    return mat

def expRendijas(proba,blancos,rendijas):
    mat = [[0.0 for x in range(blancos+rendijas+1)] for x in range(blancos+rendijas+1)]
    cada = blancos//rendijas if blancos%2==0 else (blancos+1)//(rendijas)
    repite = False if blancos%2==0 else True
    j=1
    for k in range(1,rendijas+1):
        mat[k][0]=round(proba[k-1],1)
        for i in range(j,j+cada):
            mat[i][k]= round(1/cada,1)
        j+=cada-1
        for l in range(blancos-rendijas+1,len(mat)):
            mat[l][l]=1.0
    return mat 

def expCuanticoRendijas(proba,blancos,rendijas):
    for u in range(len(proba)):
        proba[u]=(proba[u][0]**2)+(proba[u][1]**2)
    mat = [[0.0 for x in range(blancos+rendijas+1)] for x in range(blancos+rendijas+1)]
    cada = blancos//rendijas if blancos%2==0 else (blancos+1)//(rendijas)
    j=1   
    for k in range(1,rendijas+1):
        mat[k][0]=round(proba[k-1],1)
        for i in range(j,j+cada):
            mat[i][k]= round(1/cada,1)
        j+=cada-1
        for l in range(blancos-rendijas,len(mat)):
            mat[l][l]=1.0
            
    return mat

def graphStateVector(startingState):
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    numbers=[[x] for x in range(len(startingState))]
    xx=range(len(startingState))

    ax.bar(xx, startingState, width=0.8, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(numbers)

    plt.show()
    
##def main():
##    mat=[]
##    n=int(input()) 
##    for i in range(n):
##        mat.append([])
##        mat[i] = list(map(int, input().split()))
##    startingState = list(map(int, input().split()))
##    #print("startingState",startingState)
##    clicks=int(input())
####    mat=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
####    startingState=[6,2,1,5,3,10]
####    clicks=1    
##    print(canicas(mat,clicks,startingState))
##main()
