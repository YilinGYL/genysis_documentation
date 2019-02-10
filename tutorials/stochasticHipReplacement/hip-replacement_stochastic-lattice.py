#$ pip install genysis
import genysis

#easy part upload at https://studiobitonti.appspot.com/
#see upload tutorial for more details
token = "dev"
bipolar_head_filename = "hip-replacement_bipolar-head.obj"
bipolar_head_difference_tool_filename = "hip-replacement_bipolar-head_difference-1.obj"
bipolar_head_intersection_tool_filename = "hip-replacement_bipolar-head_intersection-1.obj"
femoral_stem_filename = "hip-replacement_femoral-stem.obj"
femoral_stem_difference_tool_filename = "hip-replacement_femoral-stem_difference-1.obj"
femoral_stem_intersection_tool_filename = "hip-replacement_femoral-stem_intersection-1.obj"

# this hip replacement is made of two parts, the bipolar head, which is surgically installed
# into the hip bone, and the femoral stem, which is surgically installed into the femur.
# both parts need to integrate with the bone around them, so we are adding a biocompatible
# stochastic lattice to a portion of both parts.

## BIPOLAR HEAD COMPONENT

# cut the surface off of the bipolar head
# (so we can replace it with a biocompatible stochastic lattice)
# and store it in a new file
bipolar_head_difference_output_filename = "hip-replacement_bipolar-head_difference-1-applied.obj"

genysis.boolean(
    input1=bipolar_head_filename,
    input2=bipolar_head_difference_tool_filename,
    output=bipolar_head_difference_output_filename,
    operation="difference",
    token=token)

# grab an intersection with the bipolar head
# to use as the bounds of our lattice and store it in a new file
bipolar_head_intersection_output_filename = "hip-replacement_bipolar-head_intersection-1-applied.obj"

genysis.boolean(
    input1=bipolar_head_filename,
    input2=bipolar_head_intersection_tool_filename,
    output=bipolar_head_intersection_output_filename,
    operation="intersection",
    token=token)

# create a volume lattice object
bipolar_head_lattice = genysis.volumeLattice()

# use the previously computed intersection volume as the bounds of our lattice
bipolar_head_lattice.setVolume(bipolar_head_intersection_output_filename)

# set the pore size for the lattice
bipolar_head_lattice.setPoreSize(1.0)

# tell genysis where to save the lattice object
completed_bipolar_head_lattice_filename = "hip-replacement_bipolar-head_lattice-1-applied.obj"
bipolar_head_lattice.setOutput(completed_bipolar_head_lattice_filename)

# generate the lattice (this is a large part and it might take a min or two...)
bipolar_head_lattice.runStochastic(token)

# the lattice is just a wireframe structure now
# we need to create a mesh around the wireframe in order to have a manufacturable part
bipolar_head_meshed_lattice_filename = "hip-replacement_bipolar-head_lattice-1-meshed"

bipolar_head_stl_files = genysis.marchingCube(
    lines=completed_bipolar_head_lattice_filename,
    resolution=300,
    memberThickness=0.2,
    filename=bipolar_head_meshed_lattice_filename,
    token=token)

## FEMORAL STEM COMPONENT

# cut the surface off of the bipolar head
# (so we can replace it with a biocompatible stochastic lattice)
# and store it in a new file
femoral_stem_difference_output_filename = "hip-replacement_femoral-stem_difference-1-applied.obj"

genysis.boolean(
    input1=femoral_stem_filename,
    input2=femoral_stem_difference_tool_filename,
    output=femoral_stem_difference_output_filename,
    operation="difference",
    token=token)

# grab an intersection with the bipolar head
# to use as the bounds of our lattice and store it in a new file
femoral_stem_intersection_output_filename = "hip-replacement_femoral-stem_intersection-1-applied.obj"

genysis.boolean(
    input1=femoral_stem_filename,
    input2=femoral_stem_intersection_tool_filename,
    output=femoral_stem_intersection_output_filename,
    operation="intersection",
    token=token)

# create a volume lattice object
femoral_stem_lattice = genysis.volumeLattice()

# use the previously computed intersection volume as the bounds of our lattice
femoral_stem_lattice.setVolume(femoral_stem_intersection_output_filename)

# set the pore size of the lattice
femoral_stem_lattice.setPoreSize(2.5)

# tell genysis where to save the lattice object
completed_femoral_stem_lattice_filename = "hip-replacement_femoral-stem_lattice-1-applied.obj"
femoral_stem_lattice.setOutput(completed_femoral_stem_lattice_filename)

# generate the lattice (this is a large part and it might take a min or two...)
femoral_stem_lattice.runStochastic(token)

# the lattice is just a wireframe structure now
# we need to create a mesh around the wireframe in order to have a manufacturable part
femoral_stem_meshed_lattice_filename = "hip-replacement_femoral-stem_lattice-1-meshed"

femoral_stem_stl_files = genysis.marchingCube(
    lines=completed_femoral_stem_lattice_filename,
    resolution=300,
    memberThickness=0.5,
    filename=femoral_stem_meshed_lattice_filename,
    token=token)

#the function will return a list of STL files, each one no larger than 90 MB
#high density meshes are computed distriubted for speed.

# In order to perform the final boolean operation
# we need to download the .stl files, combine them, save them as an .obj file and
# finally upload it so we can use it with genysis

# download the .stl files
for file in femoral_stem_stl_files:
    genysis.download(src=file, dest=file, token=token)

for file in bipolar_head_stl_files:
    genysis.download(src=file, dest=file, token=token)

#$ pip install numpy
import numpy
#$ pip install numpy-stl
import stl

from collections import OrderedDict

# combine all of the stls
combined_bipolar_head = numpy.concatenate(
    [stl.stl.BaseStl.load(open(filename, "rb"))[1] for filename in bipolar_head_stl_files]
)

combined_femoral_stem = numpy.concatenate(
    [stl.stl.BaseStl.load(open(filename, "rb"))[1] for filename in femoral_stem_stl_files]
)

bipolar_head_faces = combined_bipolar_head['vectors']

femoral_stem_faces = combined_femoral_stem['vectors']

del combined_bipolar_head
del combined_femoral_stem

bipolar_head_verts = OrderedDict()
bipolar_head_tris = []

femoral_stem_verts = OrderedDict()
femoral_stem_tris = []

# building vert and tri list
print("deduping verts, this could take a few minutes")
cur_v_index = 0
for face in bipolar_head_faces:
    tri = []
    for vert in face:
        v = tuple(vert)

        if v not in bipolar_head_verts:
            v_index = cur_v_index
            bipolar_head_verts[v] = v_index
            cur_v_index += 1
        else:
            v_index = bipolar_head_verts[v]

        tri.append(v_index)
    if(tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]):
        print("bipolar head tri has duplicate vertex index!")
        print("tri # " + str(len(bipolar_head_tris)))
        print(str(tri[0]) + " " + str(tri[1]) + " " + str(tri[2]))
    bipolar_head_tris.append(tri)

del bipolar_head_faces

cur_v_index = 0
for face in femoral_stem_faces:
    tri = []
    for vert in face:
        v = tuple(vert)

        if v not in femoral_stem_verts:
            v_index = cur_v_index
            femoral_stem_verts[v] = v_index
            cur_v_index += 1
        else:
            v_index = femoral_stem_verts[v]

        tri.append(v_index)
    if(tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]):
        print("femoral stem tri has duplicate vertex index!")
        print("tri # " + str(len(femoral_stem_tris)))
        print(str(tri[0]) + " " + str(tri[1]) + " " + str(tri[2]))
    femoral_stem_tris.append(tri)

del femoral_stem_faces

# wite .obj files to local folder
print("writing bipolar head")
with open(bipolar_head_meshed_lattice_filename + ".obj", 'w') as f:
    f.write("# OBJ file\n")

    print("writing verts")
    for v in list(bipolar_head_verts.items()):
        f.write("v %.8f %.8f %.8f\n" % v[0][:])

    print("writing tris")
    for t in bipolar_head_tris:
        f.write("f")
        for i in t:
            f.write(" %d" % (i + 1))
        f.write("\n")

print("writing femoral stem")
with open(femoral_stem_meshed_lattice_filename + ".obj", 'w') as f:
    f.write("# OBJ file\n")

    print("writing verts")
    for v in list(femoral_stem_verts.items()):
        f.write("v %.8f %.8f %.8f\n" % v[0][:])

    print("writing tris")
    for t in femoral_stem_tris:
        f.write("f")
        for i in t:
            f.write(" %d" % (i + 1))
        f.write("\n")

# upload the now combined meshed lattice .OBJs to the genysis server
import requests
# get the upload path for large files
upload_url = requests.get('http://studiobitonti.appspot.com/compute/getNode?t=' + token).text
upload_url += '/storage/upload?t=' + token

bipolar_files = {'file': (bipolar_head_meshed_lattice_filename, open(bipolar_head_meshed_lattice_filename, 'rb'))}

r_bipolar = requests.post(upload_url, files=bipolar_files)

femoral_files = {'file': (femoral_stem_meshed_lattice_filename, open(femoral_stem_meshed_lattice_filename, 'rb'))}

r_femoral = requests.post(upload_url, files=femoral_files)

# combine the lattices with the original shapes
completed_bipolar_head_filename = "hip-replacement_bipolar-head-with-lattice_final.obj"

results = genysis.boolean(
    input1=bipolar_head_difference_output_filename,
    input2=bipolar_head_meshed_lattice_filename + ".obj",
    output=completed_bipolar_head_filename,
    operation="union",
    token=token)

print(results)

completed_femoral_stem_filename = "hip-replacement_femoral-stem-with-lattice_final.obj"

results = genysis.boolean(
    input1=femoral_stem_difference_output_filename,
    input2=femoral_stem_meshed_lattice_filename + ".obj",
    output=completed_femoral_stem_filename,
    operation="union",
    token=token)

print(results)


# open a browser window to preview the final bipolar head
genysis.visualize(name=completed_bipolar_head_filename)
# download the final bipolar head file to the local folder
genysis.download(src=completed_bipolar_head_filename, dest=completed_bipolar_head_filename, token=token)

# open a browser window to preview the final femoral stem
genysis.visualize(name=completed_femoral_stem_filename)
# download the final femoral stem file to the local folder
genysis.download(src=completed_femoral_stem_filename, dest=completed_femoral_stem_filename, token=token)

#easy part upload at https://studiobitonti.appspot.com/
#see upload tutorial for more details
