import nashpy as nash 
import numpy as np

A=np.array([[10,0],[0,5]]) 
B=np.array([[5,0],[0,10]]) 
game=nash.Game(A,B)
print(game)
print("\nNash Equilibrium [C,H] :\n") 
ne=game.support_enumeration() 
print(list(ne))
