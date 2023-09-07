import matplotlib.pyplot as plt
from helper.loadFile import *
from scipy.linalg import svd

####################################
# VISUALIZE COMPONENT COEFFICIENTS #
####################################

# Subtract mean value from data
Y = X - np.ones((N,1))*X.mean(axis=0)
Y = Y*(1/np.std(Y,0))


# PCA by computing SVD of Y
U,S,Vh = svd(Y,full_matrices=False)

V=Vh.T
N,M = X.shape
# Compute variance explained by principal components
pcs = [0,1,2]
legendStrs = ['PC'+str(e+1) for e in pcs]
c = ['r','g','b']
bw = .2
r = np.arange(1,M+1)
for i in pcs:    
    plt.bar(r+i*bw, V[:,i], width=bw)
plt.xticks(r+bw, attributeNames)
plt.xlabel('Attributes')
plt.ylabel('Component coefficients')
plt.legend(legendStrs)
plt.grid()
plt.title('SAheart: PCA Component Coefficients')
plt.show()