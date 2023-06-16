import numpy as np

"""n= int(input('Entrer le nombre de critère '))
M=np.zeros((n,n))
M[0][0]=1
M[1][0]=5"""
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

"""A=np.array((crime,4))
table=np.array([[350000,1000,2.1,16],[275000,500,3.2,16],])
"""

print(obtain_criteria_weight(M))

def Total_item_weight(table,CR):
    for i in range(table.shape[1]):
        for j in range(table.shape[1*0]):
            table[j][i]=table[j][i]*CR[i]
    return table.sum(axis=1)


# importation de la bibliothèque
from flask import Flask
app = Flask(__name__)

@app.route('/AHP')
def test():
    print('Entrer les incidents')
    nb_crime=int(input())
    table=np.zeros((nb_crime,4))
    name=[]
    for i in range (nb_crime):
            print("Entrer les informations pour le crime ",1)
            N=input('Entrer le nome du crime ')
            name.append(N)
            table[i][0]=int(input("Enter the ranking of crime",i))
            table[i][1]=int(input("Enter the distance",i))
            table[i][2]=int(input("Enter number of victims",i))
            table[i][3]=int(input("Enter le taux de criminalité de la zone",i))

    #table=np.array([[350000,1000,2.1,16],[275000,500,3.2,16],])
    val=Total_item_weight(table,obtain_criteria_weight(M))
    maxi=val[0]
    ind=0
    for i in range(1,len(val)):    
        if maxi<val[i]:
            maxi=val[i]
            ind=i
    print(val)
    print(max(val))
    print(maxi,ind+1)
    return {"nom du crime":name[ind],'numero':ind+1}

if __name__ == '__main__':
    app.run(debug=True, port=6000)
    print("lancement")