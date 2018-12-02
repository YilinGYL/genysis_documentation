import genysis
import json

a = [["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]
pts = [[-28.918442,8.70964,1.0],[-43.438754,-2.261607,0.0],[-42.419287,10.503024,2.0],[-33.557706,-1.216382,5.0],[-36.607761,6.483151,0.0],[-44.044205,4.3235,0.0]]

t="dev"

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
#x=genysis.genLatticeUnit(3,0.2,0.3,0.7,0.3,0.8,"Example_LatticeUnit1.obj")
#x=genysis.meshReduce("Dirty_Mesh.obj","Mesh_Reduced_Example.obj",0.5)

#x=genysis.blend("Blend_Input_A.obj.obj","Blend_Input_B.obj",0.5,"out.obj")

#x=genysis.delaunay(pts)
#x=genysis.voronoi(pts)
#x=genysis.convexHull(pts)
#x=genysis.boolean("Boolean_Input_A.obj","Boolean_Input_B.obj","Boolean_Difference_Result.obj","difference")

#x=genysis.planarProjection("Body.obj",[1,-3,1],[0,0,1],[2,4],[100,100],"P_Projection_Result.obj")

#x=genysis.sphericalProjection("Head.obj",[0,0,0],[100,100],[[0,0.5],[0,0.5]],[0,1,0],"S_Proj_Result_Arm.obj")

#x=genysis.cylindricalProjection("Arm5.obj",[20,20],2,"Result.obj",[0,0,0],[[0,1],[0,1]],[1,0,0],[0,0,0])

# JT= genysis.conformalVolume()
# x=JT.genGrid()
# print(x)
# y=JT.populateLattice()

# genysis.download("Arm.obj","/test","dev")
#

volLat = genysis.volumeLattice()
volLat.setVolume("Vol_Latt_Base.obj")
volLat.setOutput("wow.obj")
volLat.stochasticLatticeStatic(t)
# print(volLat.volume)
# volLat.setOutput("wow.obj")
# volLat.setAttractor(a)
# volLat.volumeLatticeAttractor()

# latOne = genysis.surfaceLattice()
# latOne.setSurface("Base_Surface.obj")
# latOne.setOutput("works.obj")
# latOne.setAttractor(a)
# latOne.twoSurfaceLatticeStatic()

# latTwo = genysis.surfaceLattice()
# latTwo.setAttractor(a)
# latTwo.setOutput("test.obj")
# print(latTwo.attractorSet)
# latTwo.twoSurfaceAttractors()
