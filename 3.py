import nashpy as nash 
import numpy as np

A=np.array([[1,-1],[-1,1]]) 
B=np.array([[-1,1],[1,-1]]) 
game=nash.Game(A,B)
print(game)
print("\nNash Equilibrium [Head , Tail ] :\n") 
ne=game.support_enumeration() 
print(list(ne))
