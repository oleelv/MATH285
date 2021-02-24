from dolfin import *
from mshr import *
from matplotlib import pyplot
import numpy as np
import scipy.io

# Create empty Mesh
N = 32

mesh = RectangleMesh(Point(0.0,0.0),Point(1.0,1.0),N,N)

V = FunctionSpace(mesh, 'CG', 1)

n = V.dim()
d = mesh.geometry().dim()

dof_coordinates = V.tabulate_dof_coordinates()
dof_coordinates.resize((n,d))

#Define variational forms
u = TrialFunction(V)
v = TestFunction(V)

a = (inner(grad(u), grad(v)) + u*v)*dx
m = u*v*dx

#Assemble matrices
A = assemble(a)
M = assemble(m)

np.save('A.npy', A.array())
np.save('M.npy', M.array())
np.save('coords.npy', dof_coordinates)
