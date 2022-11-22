import nashpy as nash 
import numpy as np

A=np.array([[10,0],[5,5]]) 
B=np.array([[10,5],[0,5]]) 
game=nash.Game(A,B)
print(game)
print("\nNash Equilibrium [Deer,Rabbit] :\n") 
ne=game.support_enumeration() 
print(list(ne)) 