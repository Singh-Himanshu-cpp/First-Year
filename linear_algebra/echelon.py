# first create matrix.txt
def echelon(m):
    num_pivots=0
    for j in range(len(m[0])):   # going column wise
        for i in range(num_pivots,len(m)):
            for k in range(i,len(m)): # cheching if pivots exist in the row
                if m[k][j]:
                    m[k],m[i]=m[i],m[k]
                    m[i]=[e/m[i][j] for e in m[i]] # making pivot position 1
                    break
        if num_pivots<len(m) and m[num_pivots][j]:
            num_pivots+=1
            pivotcolumns.append(j+1)
        for i in range(num_pivots,len(m)):
            if m[i][j]:
                m[i]=[m[i][k]-m[num_pivots-1][k] for k in range(len(m[i]))]
                for k in range(len(m[i])):      # removing aproximations made by float of python
                    if -0.00001<m[i][k]<0.00001:
                        m[i][k]=0
    print("echelon form is"+str(m)+"\n")
def RREF(m):
    for j in range(len(m[0])):
        if (j+1) in pivotcolumns:
            for i in range(len(m)):
                num=m[i][j]
                if i<pivotcolumns.index(j+1) and m[i][j]:
                    m[i]=[m[i][k]-m[pivotcolumns.index(j+1)][k]*num for k in range(len(m[i]))]
                    for k in range(len(m[i])):      # removing aproximations made by float of python
                        if -0.00001<m[i][k]<0.00001:
                            m[i][k]=0
    print("RREF form is"+str(m)+"\n")
def solution(m):
    check=1
    pivot=[]
    # since row of zeros does not have any affect on the solution
    zero_row=[0 for i in range(len(m[0]))]
    while(zero_row in m):
        m.remove(zero_row)
    # going column wise
    for i in range(len(m[0])):
        count=0
        l=[]
        for j in range(len(m)):
            if m[j][i] and j==len(pivot): 
        # the first pivot will be in first row and second pivot in second row and so on 
                count+=1
        if count==1:
            pivot.append(i+1)
        else:
            check=0
            print("x"+str(i+1),end=" ")
            l=[0 for i in range(len(m[0]))]
            l[i]=1
            index=0
            for k in pivot:
                if k<i+1:
                    l[k-1]=-m[index][i]
                    index+=1
            print(l,end=" + ")
    print("0")
    if check:
        print("only trivial solution exists")
    print("\npivots are column ",end="")
    print(pivot)
# main
f=open("matrix.txt")
m=[]
for l in f:
    row=[int(i) for i in l.split()]
    m.append(row)
f.close()
# convering to echelon
pivotcolumns=[]
echelon(m)
# convering to RREF
RREF(m)
# printing the homogenous solution
solution(m)
