#$ pip install genysis
import genysis

#easy part upload at https://studiobitonti.appspot.com/
#see upload tutorial for more details
token = "dev"
connecting_rod_filename = "connecting-rod.obj"
difference_tool_filename = "connecting-rod_difference-tool-1.obj"
intersection_tool_filename = "connecting-rod_intersection-tool-1.obj"

# cut a hole out of the original solid connecting rod
# and store it in a new file
difference_output_filename = "connecting-rod_difference-1-applied.obj"

genysis.boolean(
    input1=connecting_rod_filename,
    input2=difference_tool_filename,
    output=difference_output_filename,
    operation="difference",
    token=token)

# grab an intersection with the original solid connecting rod
# to use as the bounds of our lattice and store it in a new file
intersection_output_filename = "connecting-rod_intersection-1-applied.obj"

genysis.boolean(
    input1=connecting_rod_filename,
    input2=intersection_tool_filename,
    output=intersection_output_filename,
    operation="intersection",
    token=token)

# create a low density lattice unit for the middle of the cutout
low_density_unit_filename = "low_density_lattice_unit.obj"

genysis.genLatticeUnit(
    case=3,
    chamfer=1.0,
    centerChamfer=0.0,
    bendIn=1.0,
    cBendIn=0.0,
    connectPt=0.0,
    output=low_density_unit_filename,
    token=token)

# create a high density lattice unit for the edges of the cutout
high_density_unit_filename = "high_density_lattice_unit.obj"

genysis.genLatticeUnit(
    case=3,
    chamfer=0.0,
    centerChamfer=0.0,
    bendIn=0.5,
    cBendIn=0.0,
    connectPt=0.0,
    output=high_density_unit_filename,
    token=token)

# create a volume lattice object
cutoutLattice = genysis.volumeLattice()

# use the previously computed intersection volume as the bounds of our lattice
cutoutLattice.setVolume(intersection_output_filename)

# set the default component/unit for the lattice
cutoutLattice.setComponent(low_density_unit_filename)

# set the size of one lattice unit
cutoutLattice.setComponentSize(5.0)

# define some planes to use as attractors [normX, normY, normZ, distanceFromOrigin]
top_plane_attractor =    [0,  0,  1, 82.099785]
bottom_plane_attractor = [0,  0, -1, 162.403183]
left_plane_attractor =   [0, -1,  0, 10.864898]
right_plane_attractor =  [0,  1,  0, -11.994245]

# add our attractors to cause the lattice to be more solid at the edges of the volume
#top
cutoutLattice.addPointAttractor(component=high_density_unit_filename, point=[0,0,-120], range=10.0)
# cutoutLattice.addPlaneAttractor(component=high_density_unit_filename, plane=top_plane_attractor, range=0.1)
#bottom
# cutoutLattice.addPlaneAttractor(component=high_density_unit_filename, plane=bottom_plane_attractor, range=0.1)
# #left
# cutoutLattice.addPlaneAttractor(component=high_density_unit_filename, plane=left_plane_attractor, range=0.1)
# #right
# cutoutLattice.addPlaneAttractor(component=high_density_unit_filename, plane=right_plane_attractor, range=1.0)

# tell genysis where to save the lattice object
completed_lattice_filename = "connecting-rod_lattice-1-applied.obj"
cutoutLattice.setOutput(completed_lattice_filename)

# generate the lattice (this is a large part and it might take a min or two...)
cutoutLattice.run(token)

# the lattice is just a wireframe structure now
# we need to create a mesh around the wireframe in order to have a manufacturable part
meshed_lattice_filename = "connecting-rod_lattice-1-meshed"

stl_files = genysis.marchingCube(
    lines=completed_lattice_filename,
    resolution=300,
    memberThickness=0.4,
    filename=meshed_lattice_filename,
    token=token)

#the function will return a list of STL files, each one no larger than 90 MB
#high density meshes are computed distriubted for speed.
#for example...
# [
#     "connecting-rod_lattice-1-meshed_0.stl",
#     "connecting-rod_lattice-1-meshed_1.stl",
#     "connecting-rod_lattice-1-meshed_2.stl",
#     "connecting-rod_lattice-1-meshed_3.stl",
#     "connecting-rod_lattice-1-meshed_4.stl"
# ]

# In order to perform the final boolean operation
# we need to download the .stl files, combine them, save them as an .obj file and
# finally upload it so we can use it with genysis

# download the .stl files
for file in stl_files:
    genysis.download(src=file, dest=file, token=token)

#$ pip install numpy
import numpy
#$ pip install numpy-stl
import stl
#$ pip install tqdm
from tqdm import tqdm
from pprint import pprint

from collections import OrderedDict

from sys import getsizeof

# combine all of the stls
combined = numpy.concatenate(
    [stl.stl.BaseStl.load(open(filename, "rb"))[1] for filename in stl_files]
)

pprint(combined)

faces = combined['vectors']
print("size of faces in KB: " + str(faces.nbytes/1000))

del combined

verts = OrderedDict()
tris = []

cur_v_index = 0

# building vert and tri list
print("deduping verts, this could take a few minutes")
for face in faces:
    tri = []
    for vert in face:
        v = tuple(vert)

        if v not in verts:
            v_index = cur_v_index
            verts[v] = v_index
            cur_v_index += 1
        else:
            v_index = verts[v]

        tri.append(v_index)
    tris.append(tri)

del faces

print("size of verts in KB: " + str(getsizeof(verts)/1000))
print("size of tris in KB: " + str(getsizeof(tris)/1000))

# wite .obj file
with open(meshed_lattice_filename + ".obj", 'w') as f:
    f.write("# OBJ file\n")
    for v in tqdm(list(verts.items()[0]), desc="writing verts"):
        f.write("v %.4f %.4f %.4f\n" % v[:])
    for t in tqdm(tris, desc="writing tris"):
        f.write("f")
        for i in t:
            f.write(" %d" % (i + 1))
        f.write("\n")

genysis.upload(src=meshed_lattice_filename + ".obj", token=token)

# combine the lattice with the solid connecting rod that we cut a hole out of
completed_connecting_rod_filename = "connected-rod-with-lattice_final.obj"

results = genysis.boolean(
    input1=difference_output_filename,
    input2=meshed_lattice_filename + ".obj",
    output=completed_connecting_rod_filename,
    operation="union",
    token=token)

print(results)

genysis.visualize(name=completed_connecting_rod_filename)
genysis.download(src=completed_connecting_rod_filename, dest=completed_connecting_rod_filename, token=token)

#easy part upload at https://studiobitonti.appspot.com/
#see upload tutorial for more details
