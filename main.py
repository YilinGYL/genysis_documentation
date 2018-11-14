import genysis
import json

#x=genysis.stochasticLattice("S_lattice.obj",0.5,"S_lattice_Result.obj","DEV")

#x= genysis.volumeLattice("Example_LatticeUnit.obj","Vol_Latt_Base.obj",1.2,"vol_Lattice_Example.obj","DEV")

x = genysis.volumeLattice_attractor("unit_1.obj","Vol.obj",0.5,"vol_exmple_2.obj","DEV")
print(x)
