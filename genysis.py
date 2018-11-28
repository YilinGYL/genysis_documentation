import requests
import json
import ast

token = ""

#all projections need testing
def cylindricalProjection(target,center,resolution,range,rotateAxis,startDir,height,output):
    url ="https://studiobitonti.appspot.com/cylindricalProjection"
    payload = {"target":target,"center":center,"resolution":resolution,"range":range,"rotateAxis":rotateAxis,"start_dir":startDir,"height":height,"output":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def sphericalProjection(target,center,resolution,range,rotateAxis,output):
    url ="https://studiobitonti.appspot.com/sphericalProjection"
    payload = {"target":target,"center":center,"resolution":resolution,"range":range,"rotateAxis":rotateAxis,"output":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def planarProjection(target,center,direction,size,resolution,output):
    url ="https://studiobitonti.appspot.com/planeProjection"
    payload = {"target":target,"center":direction,"size":size,"resolution":resolution,"output":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

#error
def boolean(input1,input2,output,operation): #operations are Union, Interset and Difference
    url ="https://studiobitonti.appspot.com/boolean"
    payload = {"input1":input1,"input2":input2,"output":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def convexHull(a):
    url ="https://studiobitonti.appspot.com/convexHull"
    payload = {"points":a,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def voronoi(a):
    url ="https://studiobitonti.appspot.com/voronoi"
    payload = {"points":a,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def delaunay(a):
    url ="https://studiobitonti.appspot.com/delaunay"
    payload = {"points":a,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def blend(compA,compB,value,output):
    url ="https://studiobitonti.appspot.com/blend"
    payload = {"compA":compA,"compB":compB,"value":value,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

#not working Li will check backend
def meshSplit(target,output):
    url ="https://studiobitonti.appspot.com/meshSplit"
    payload = {"target":target,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def meshReduce(target,output,portion):
    url ="https://studiobitonti.appspot.com/meshreduction"
    payload = {"target":target,"portion":portion,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def genLatticeUnit(case,chamfer,centerChamfer,bendIn,cBendIn,connectPt,output):
# Case: Is an integer value between 0 - 7,  defining different type of lattice units.
# Chamfer: Is a float value between 0 to 0.5 defining the angle of chamfer of the corners.
# Center Chamfer: Is a float value between 0 to 0.5 defining the angle of chamfer from the center.
# Bendln: Is a float value between 0 and 1, defining angle bend of the lines.
# cBendln:  Is a float value between 0 and 1,defining the central bend of the lines.
# Connect Pt:  Is a float value between 0 and 1, defining the connection points.
    url = "https://studiobitonti.appspot.com/latticeUnit"
    payload = {"case":case,"chamfer":chamfer,"centerChamfer":centerChamfer,"bendIn":bendIn,"cBendIn":cBendIn,"connectPt":connectPt,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text


def parseComponents(a):
    bodyMain=""
    for i in range(len(a)):
        body="{\"component\":\"%s\",\"attractor\":{\"point\":%s,\"range\":%s}}" % (a[i][0],a[i][1],a[i][2])
        if(i>0):
            bodyMain+=","+body
        else:
            bodyMain+=body
    final="\"blendTargets\":["+bodyMain+"]}"
    return final

def marchingCube(lines,resolution,memberThickness,filename):

    url = "https://studiobitonti.appspot.com/marchingCube"
    payload = {"lines":lines,"resolution":resolution,"memberThickness":memberThickness,"filename":filename,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

class volumeLattice:
    def __init__(self): #set global variables
        #URL is always this.
        #self.url = "https://studiobitonti.appspot.com/stochasticLattice"
        self.url = "https://studiobitonti.appspot.com/volumeLattice"
        #variables that need to be set by the user.
        self.poreSize=.02
        self.volume=""
        self.output=""
        self.component="unit_1.obj"
        self.componentSize=1
        #attactors will be formated as an 2D array "["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]"
        #default values are files included in sample repo.
        self.attractorSet=[["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]

#functions for seting key variables

    def setAttractor(self,a): #attractors are optional (blended lattices only)
        self.attractorSet=a
    def setOutput(self,output):#file name that you want to save out
        self.output=output
    def setVolume(self,volume):#base surface
        self.volume=volume
    def setPoreSize(self,pore):#pore size for stochastic Lattice
        self.poreSize=pore
    def setComponentSize(self,cellHeight):#size of componet in a static or graded grid
        self.componentSize=cellHeight

#lattice generation functions

    def stochasticLatticeStatic(self):
        self.url = "https://studiobitonti.appspot.com/stochasticLattice"
        payload = {"volume":self.volume,"poreSize":self.poreSize,"filename":self.output,"t":token}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        self.url = "https://studiobitonti.appspot.com/volumeLattice"
        return r.text

    def volumeLatticeStatic(self):
        payload = {"component":self.component,"volume":self.volume,"componentSize":self.componentSize,"filename":self.output,"t":token}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        return r.text

    def volumeLatticeAttractor(self):
        #get attractor information
        att=parseComponents(self.attractorSet)
        payload = "{\"component\":\"%s\",\"volume\":\"%s\",\"componentSize\":%s,\"filename\": \"%s\",\"t\":\"%s\",%s" % (self.component,self.volume,self.componentSize,self.output,token,att)
        print(payload)
        #convert paylod to dictionary
        dict=ast.literal_eval(payload)
        #make post request
        r = requests.post(self.url,json=dict)
        print(r.text)
        return r.text

class surfaceLattice:
    def __init__(self): #set global variables
        #URL is always this.
        self.url = "https://studiobitonti.appspot.com/surfaceLattice"
        #Always True
        self.autoScale="true"
        self.ESIPLON=1
        self.bin="true"
        #variables that need to be set by the user.
        self.output = "twoSurfaceLattice_attractor_output.obj"
        self.cellHeight=1
        #attactors will be formated as an 2D array "["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]"
        #default values are files included in sample repo.
        self.attractorSet=[["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]
        self.component="unit_1.obj"
        self.base="Base_Surface.obj"
        self.ceil="Ciel_CompB.obj"

#functions for seting key variables

    def setAttractor(self,a): #attractors are optional (blended lattices only)
        self.attractorSet=a
    def setBin(self,bin):
        self.bin=bin
    def setEspilon(self,espilon):
        self.ESIPLON=espilon
    def setOutput(self,output):#file name that you want to save out
        self.output=output
    def setSurface(self,base):#base surface
        self.base=base
    def setTopSurface(self,ceil):#Top surface
        self.ceil=ceil
    def setCellHeight(self,cellHeight):#if no top surface is defined set a cell height. Else it will be set to 1
        self.cellHeight=cellHeight

#lattice generation functions

    def twoSurfaceAttractors(self):#Lattice between two surfaces with attractors for blended lattice
        #get attractor information
        att=parseComponents(self.attractorSet)
        payload = "{\"component\":\"%s\",\"base\":\"%s\",\"cellHeight\":%s,\"filename\": \"%s\",\"t\":\"%s\",%s" % (self.component,self.base,self.cellHeight,self.output,token,att)
        print(payload)
        #convert paylod to dictionary
        dict=ast.literal_eval(payload)
        #make post request
        r = requests.post(self.url,json=dict)
        print(r.text)
        return r.text

    def oneSurfaceLatticeAttractors(self):#Lattice on one surface with a constant offset with attractors for blended lattice
        #get attractor information
        att=parseComponents(self.attractorSet)
        payload = "{\"component\":\"%s\",\"base\":\"%s\",\"cellHeight\":%s,\"filename\": \"%s\",\"t\":\"%s\",%s" % (self.component,self.base,self.cellHeight,self.output,token,att)
        print(payload)
        #convert paylod to dictionary
        dict=ast.literal_eval(payload)
        #make post request
        r = requests.post(self.url,json=dict)
        print(r.text)
        return r.text

    def surfaceLatticeStatic(self): #Lattice on one surface with a constant offset
        payload = {"component":self.component,"base":self.base,"cellHeight":self.cellHeight,"filename":self.output,"t":token}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        return r.text

    def twoSurfaceLatticeStatic(self):#Lattice structure between two surfaces
        payload = {"component":self.component,"base":self.base,"cellHeight":self.cellHeight,"filename":self.output,"t":token,"ceil":self.ceil,"autoScale":self.autoScale,"ESIPLON":self.ESIPLON,"bin":self.bin}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        return r.text
