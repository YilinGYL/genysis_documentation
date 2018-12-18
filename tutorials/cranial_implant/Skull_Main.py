#$ pip install genysis
import genysis

#easy part upload at https://studiobitonti.appspot.com/
#see upload tutorial for more details

token = "dev"
MPfilename = "implant.obj"
cellName = "cell_1.obj"

#create a lattice unit
#genLatticeUnit(case,chamfer,centerChamfer,bendIn,cBendIn,connectPt,output,token):
#bug:function is currently not accepting 0.0 as a value
genysis.genLatticeUnit(7,0.01,0.01,0.01,0.01,1.0,cellName,token)

#create a surface lattice class
cranial =genysis.surfaceLattice()

#set the values needed for this function
cranial.setSurface("Skull_Srf.obj")
cranial.setCellHeight(0.1)
cranial.setOutput(MPfilename)
cranial.setComponent(cellName)

#Generate the lattice. It will be saved as implant.obj
cranial.run(token)

#the function will return a list of STL filesself.
#high density meshes are computed distriubted for speed.
final=genysis.marchingCube(MPfilename,900,0.01,"implantOutput",token)
print(final)

#Now lets generate one with a gradient
#First set up a new lattice component to blend into
newBlendTarget = "cell_2.obj"
genysis.genLatticeUnit(7,0.01,0.01,0.01,1.0,1,newBlendTarget,token)

#set the values needed for this function
cranial.addPointAttractor(newBlendTarget,point=[1.6,90.4,0.6],range=2)

cranial.setOutput("implant_2.obj")

#generate new lattive with attractor.
cranial.run(token)

#the function will return a list of STL filesself.
#high density meshes are computed distriubted for speed.
#for example...
#["implantOutputV2_5.stl","implantOutputV2_4.stl","implantOutputV2_3.stl","implantOutputV2_0.stl","implantOutputV2_1.stl","implantOutputV2_2.stl"]
final=genysis.marchingCube("implant_2.obj",900,0.01,"implantOutputV2",token)
print(final)
