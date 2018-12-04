#$ pip install genysis
import genysis

#easy part upload at https://studiobitonti.appspot.com/
#see upload tutorial for more details

token = "dev"
MPfilename = "mechP.obj"

#create a volume lattice object
mechP = genysis.volumeLattice()

#set the values needed for this function
mechP.setVolume("Part.obj")
mechP.setPoreSize(1.5) #units are mm
mechP.setOutput(MPfilename)

#generate the lattice (this is a large part and it might take a min or two...)
mechP.stochasticLatticeStatic(token)

#apply marchingCube function to transform the lattice into a mesh for 3D print.
#marchingCube(lines,resolution,memberThickness,filename,token):
final=genysis.marchingCube(MPfilename,700,0.25,"mechOutput",token)

#the function will return a list of STL filesself.
#high density meshes are computed distriubted for speed.
#for example...
# ["mechOutput_2.stl","mechOutput_4.stl","mechOutput_0.stl","mechOutput_3.stl",
#"mechOutput_5.stl","mechOutput_1.stl","mechOutput_6.stl"]

print(final)

#easy part upload at https://studiobitonti.appspot.com/
#see upload tutorial for more details
