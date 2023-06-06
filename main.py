import numpy as np

n= int(input('Entrer le nombre de critère '))
M=np.zeros((n,n))
M[0][0]=1
M[1][0]=5
M=np.array([[1,5,4,7],[1/5,1,2,3],[1/4,1/2,1,3],[1/7,1/3,1/3,1]])
S=M.sum(axis=0)

N=np.array([[1,5,4,7],[1/5,1,2,3],[1/4,1/2,1,3],[1/7,1/3,1/3,1]])


def normalize_pair(A):
    M=A

    S=M.sum(axis=0)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[j][i]=M[j][i]/S[i]
    return M

def calculte_criteria_weight(A):
    return A.mean(axis=1)

def calculate_criteria_sum(M,B):
    Mn=normalize_pair(M)
    print(Mn)
    print("----------------")
    print(B)
    S=calculte_criteria_weight(Mn)
    
    for i in range(Mn.shape[0]):
        for j in range(Mn.shape[1]):
            B[j][i]=B[j][i]*S[i]
    return np.array([B.sum(axis=1),S])

 
#print(calculate_criteria_sum(M,N))

def calculate_lambda_max(Matrix):
    R=np.zeros((1,Matrix.shape[1]))
    for j in range(Matrix.shape[1]):
        R[0][j]=Matrix[0][j]/Matrix[1][j]
    return R.mean()


def calculate_CI(Matrix):
    l=calculate_lambda_max(Matrix)
    return(l-Matrix.shape[1])/(Matrix.shape[1]-1)

def calculate_CR(Matrix):
    RI=[0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49]
    return calculate_CI(Matrix)/RI[Matrix.shape[1]-1]


def check_consistency(Matrix):
    if(calculate_CR(Matrix)<0.1):
        print("Good consistency")
    else:
        print("Not good")

"""R=calculate_criteria_sum(M,N)
print(calculate_lambda_max(R))
print(calculate_CR(R))
check_consistency(R)"""
crime=2

def obtain_criteria_weight(Matrix):
    M=normalize_pair(Matrix)
    return calculte_criteria_weight(M)

A=np.array((crime,4))

table=np.array([[350000,1000,2.1,16],[275000,500,3.2,16],])


print(obtain_criteria_weight(M))

def Total_item_weight(table,CR):
    for i in range(table.shape[1]):
        for j in range(table.shape[1*0]):

            table[j][i]=table[j][i]*CR[i]
    return table.sum(axis=1)


print(Total_item_weight(table,obtain_criteria_weight(M)))