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
genysis.genLatticeUnit(7,0.5,0.01,1.0,0.01,0.01,cellName,token)

#create a surface lattice class
cranial =genysis.surfaceLattice()
cranial.setSurface("Skull_Srf.obj")
cranial.setCellHeight(0.1)
cranial.setOutput(MPfilename)
cranial.setComponent(cellName)
cranial.surfaceLatticeStatic(token)

final=genysis.marchingCube(MPfilename,900,0.01,"implantOutput",token)
print(final)

#Now lets generate one with a gradient
newBlendTarget = "cell_2.obj"
genysis.genLatticeUnit(7,0.01,0.01,0.01,0.01,0.01,newBlendTarget,token)
attractorCenter = [1.4,89.89,0.5]
radius = 4
attractor=[[newBlendTarget,attractorCenter,radius]]

cranial.setAttractor(attractor)
cranial.setOutput("implant_2.obj")
cranial.oneSurfaceLatticeAttractors(token)

final=genysis.marchingCube("implant_2.obj",900,0.01,"implantOutputV2",token)
print(final)
