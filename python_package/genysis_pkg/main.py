import genysis
import json



## FILE MANAGE MENTS
# genysis.upload('SOMEFILES.obj','dev')
# genysis.download('SOMEFILES.obj','TARGET_LOCATION.obj','dev')
# files = genysis.listFiles('dev')
# print(files)



## VISUALIZER
# genysis.visualize('work.obj','dev')



## MESH REDUCE
# x=genysis.meshReduce("Dirty_Mesh.obj","Mesh_Reduced_Example.obj",0.9,"dev")
# genysis.visualize("Mesh_Reduced_Example.obj","dev")



## BLEND
# the component mesh need to be updated, there is a but when use value 0
# x=genysis.blend(compA="Blend_Input_A.obj",compB="Blend_Input_B.obj",value=0.8,output="blend.obj",token="dev")
# genysis.visualize("blend.obj",'dev')



## MESH SPLIT
# results = genysis.meshSplit("Combo_Mesh.obj","Mesh_Split_Example","dev")
# for r in results:
#     print(r)
#     genysis.visualize(r,"dev")



## NUMERICALS
# TODO: probably add visualizing feature for these
# pts = [[-28.918442,8.70964,1.0],[-43.438754,-2.261607,0.0],[-42.419287,10.503024,2.0],[-33.557706,-1.216382,5.0],[-36.607761,6.483151,0.0],[-44.044205,4.3235,0.0]]
# x=genysis.delaunay(pts,"dev")
# x=genysis.voronoi(pts,"dev")
# x=genysis.convexHull(pts,'dev')



## BOOLEAN
# genysis.boolean(input1="Boolean_Input_A.obj",input2="Boolean_Input_B.obj",output="Boolean_Result.obj",operation="difference",token="dev")
# genysis.visualize("Boolean_Result.obj",'dev')



## PLANAR PROJECT
# genysis.planarProjection(target="Body.obj",center=[1,-3,1],direction=[0,0,1],size=[2,4],resolution=[50,50],output="Result.obj",token="dev")
# genysis.visualize("Result.obj",'dev')



## SPHERICAL PROJECTION
# genysis.sphericalProjection(target="Head.obj",resolution=[20,20],output="Result.obj",token="dev",range=[[0,1],[0,0.5]],rotationAxis=[0,1,0])
# genysis.visualize("Result.obj",'dev')



## CYLINDRICAL PROJECTION
# genysis.cylindricalProjection(target="Arm5.obj",resolution=[20,20],height=2,output="Result.obj",token="dev",range=[[0,0.5],[0,1]])
# genysis.visualize("Result.obj",'dev')



## LATTICE UNIT GENERATION
# genysis.genLatticeUnit(7,0.0,0,0,0,0,'cell_1.obj','dev')
# genysis.visualize('cell_1.obj','dev')

# genysis.genLatticeUnit(7,1,0,0,0,0,'cell_2.obj','dev')
# genysis.visualize('cell_2.obj','dev')

# genysis.latticeUnitDesign()



## SURFACE LATTICE
# surfaceLattice = genysis.surfaceLattice()
# surfaceLattice.setSurface("Base_Surface.obj")
# surfaceLattice.setCellHeight(0.2)
# surfaceLattice.setComponent("cell_1.obj")
# surfaceLattice.setOutput("work.obj")
# surfaceLattice.addPointAttractor(component="cell_2.obj",point=[2.8,8,2.7],range=5)
# surfaceLattice.addCurveAttractor(component="unit_1.obj",curve=[[2.8,8,2.7],[-3.3,8,2.7],[-3.3,14,6]],range=2)
# surfaceLattice.run("dev")



## CONFORMAL LATTICE
# TODO: add function for visualizing grid
# conformalLattice = genysis.conformalLattice()
# conformalLattice.setSurfaces("Skate.json")
# conformalLattice.setUVW(65,18,3)
# conformalLattice.setGridOutput("Skate_Grid.json")
# conformalLattice.genGrid("dev")
# conformalLattice.setComponent('cell_1.obj')
# conformalLattice.setOutput('conformalLattice.obj')
# conformalLattice.addPlaneAttractor(component="cell_2.obj",plane=[0,1,0,-5],range=10)
# conformalLattice.populateLattice("dev")
# genysis.visualize('conformalLattice.obj','dev')




## STOCHASTIC LATTICE 
# TODO:this is taking too long and inacurate, needs optimization
# volLat = genysis.volumeLattice()
# volLat.setVolume("Body.obj")
# volLat.setOutput("wow.obj")
# volLat.setPoreSize(0.1)
# volLat.runStochastic("dev")
# genysis.visualize("wow.obj","dev")



## VOLUME LATTICE 
# TODO:it's buggy when components size gets small, also needs a limiter
# volLat = genysis.volumeLattice()
# volLat.setVolume("Body.obj")
# volLat.setOutput("wow.obj")
# volLat.setComponentSize(0.5)
# volLat.setComponent('cell_1.obj')
# volLat.run("dev")
# genysis.visualize("wow.obj","dev")



## MARCHING CUBES
# debug why preview is not working
# results = genysis.marchingCube("Meshing_example.obj",150,0.03,"Marching_Cube_Example","dev")
# for r in results:
#     print(r)
#     genysis.visualize(r,"dev")



