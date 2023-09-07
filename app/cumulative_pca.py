import matplotlib.pyplot as plt
from helper.loadFile import *
from scipy.linalg import svd

############################
# VISUALIZE CUMULATIVE PCA #
############################

# Subtract mean value from data
Y = X - np.ones((N,1))*X.mean(axis=0)
Y = Y*(1/np.std(Y,0))


# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)

rho = (S*S) / (S*S).sum() 

threshold = 0.9

# Plot variance explained
plt.figure()
plt.plot(range(1,len(rho)+1),rho,'x-')
plt.plot(range(1,len(rho)+1),np.cumsum(rho),'o-')
#plt.plot([1,len(rho)],[threshold, threshold],'k--')
plt.title('Variance explained by principal components');
plt.xlabel('Principal component');
plt.ylabel('Variance explained');
plt.legend(['Individual','Cumulative','Threshold'])
plt.grid()
plt.show()