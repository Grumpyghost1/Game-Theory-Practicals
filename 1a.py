import nashpy as nash 
import numpy as np

A=np.array([[-3,0],[-4,-1]])
B=np.array([[-3,-4],[0,-1]])
PrisonersD=nash.Game(A,B)
print(PrisonersD)
print("\nNash Equilibrium [Confess,Deny] :\n") 
ne=PrisonersD.support_enumeration() 
print(list(ne))