import genysis
import json

a = [["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]

genysis.token="dev"

#x=genysis.stochasticLattice("S_lattice.obj",0.5,"S_lattice_Result.obj")

#x= genysis.volumeLattice("Example_LatticeUnit.obj","Vol_Latt_Base.obj",1.2,"vol_Lattice_Example.obj","DEV")

#x = genysis.volumeLattice_attractor("unit_1.obj","Vol.obj",0.5,"vol_exmple_2.obj","DEV","unit_0.obj",[0,0,0],2)

#x= genysis.surfaceLattice("Lattice_Unit.obj","Base_Surface.obj",1,"Surface_Lattice_Example.obj","DEV")

#x= genysis.twoSurfaceLattice("Lattice_Unit.obj","Base_Surface.obj",1,"Surface_Lattice_Example.obj","dev","Ciel_CompA.obj","true",1,"false")

#x= genysis.marchingCube("Meshing_example.obj",150,0.02,"Marching_Cube_Example","dev")

#x=genysis.surfaceLattice_attractor("unit_0.obj","surface_simple.obj",5,"surfaceLattice.obj","dev","unit_0.obj","unit_1.obj",[0,0,0],[4,36,22],2,20)

#x=genysis.twoSurfaceLattice_attractor("unit_1.obj","Base_Surface.obj","true","Ciel_CompB.Obj",1,"surfaceLattice.obj","dev","unit_0.obj",[0,0,0],8)

#x=genysis.surfaceLattice_attractor_T("unit_0.obj","surface_simple.obj",5,"surfaceLattice.obj","dev",a)


#x=genysis.twoSurfaceLattice_attractor_T("unit_1.obj","Base_Surface.obj","Ciel_CompB.Obj",a)

latOne = genysis.surfaceLattice()
latOne.setSurface("Base_Surface.obj")
latOne.setOutput("works.obj")
latOne.setAttractor(a)
latOne.surfaceLatticeOffset()

# latTwo = genysis.surfaceLattice()
# latTwo.setAttractor(a)
# latTwo.setOutput("test.obj")
# print(latTwo.attractorSet)
# latTwo.twoSurfaceAttractors()
