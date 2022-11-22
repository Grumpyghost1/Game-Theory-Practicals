import nashpy as nash 
import numpy as np

A=np.array([[5,-5],[0,10]]) 
B=np.array([[0,5],[10,-5]])
game=nash.Game(A,B)
print(game)
print("\nNash Equilibrium [Left ,Right] :\n") 
ne=game.support_enumeration() 
print(list(ne))