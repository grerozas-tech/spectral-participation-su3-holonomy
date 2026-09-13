"""Exact rank-eight certificate for the curvature-jet algebra in the paper."""
import sympy as sp
M = sp.Matrix([
[7,28,0,28,0,0,693,0],
[-5,-80,0,-80,0,0,180,0],
[0,0,5,0,95,0,0,85],
[0,-15,0,15,0,95,-340,0],
[0,0,16,0,-32,0,0,104],
[0,48,0,-48,0,32,416,0],
[0,0,14,0,-238,0,0,-329],
[0,-42,0,42,0,-238,1316,0],
])
print('rank =', M.rank())
print('det  =', M.det())
assert M.rank() == 8
assert M.det() == 2822930611200000
