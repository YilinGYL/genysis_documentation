import requests
import json
import ast

token = ""

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

def stochasticLattice(volume,poreSize,filename):

    url = "https://studiobitonti.appspot.com/stochasticLattice"
    payload = {"volume":volume,"poreSize":poreSize,"filename":filename,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def volumeLattice(component,volume,componentSize,filename):

    url = "https://studiobitonti.appspot.com/volumeLattice"
    payload = {"component":component,"volume":volume,"componentSize":componentSize,"filename":filename,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def volumeLattice_attractor(component,volume,componentSize,filename,compA,vecA,rangeA):

    url = "https://studiobitonti.appspot.com/volumeLattice"
    payload = {"component":component,"volume":volume,"componentSize":componentSize,"filename":filename,"t":token,"blendTargets":[{"component":compA,"attractor":{"point":vecA,"range":rangeA}}]}
    r = requests.post(url,json=payload)
    return r.text

def surfaceLattice(component,base,cellHeight,filename):

    url = "https://studiobitonti.appspot.com/surfaceLattice"
    payload = {"component":component,"base":base,"cellHeight":cellHeight,"filename":filename,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

# def twoSurfaceLattice(component,base,cellHeight,filename,ceil,autoScale,ESIPLON,bin):
#
#     url = "https://studiobitonti.appspot.com/surfaceLattice"
#     payload = {"component":component,"base":base,"cellHeight":cellHeight,"filename":filename,"t":token,"ceil":ceil,"autoScale":autoScale,"ESIPLON":ESIPLON,"bin":bin}
#     print(json.dumps(payload))
#     r = requests.post(url,json=payload)
#     return r.text

def twoSurfaceLattice(component,base,cellHeight,filename,ceil,autoScale,ESIPLON,bin):

    url = "https://studiobitonti.appspot.com/surfaceLattice"
    payload = {"component":component,"base":base,"cellHeight":cellHeight,"filename":filename,"t":token,"ceil":ceil,"autoScale":autoScale,"ESIPLON":ESIPLON,"bin":bin}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def surfaceLattice_attractor(component,base,cellHeight,filename,compA,compB,vecA,vecB,rangeA,rangeB):

    url = "https://studiobitonti.appspot.com/surfaceLattice"
    payload = {"component":component,"base":base,"cellHeight":cellHeight,"filename":filename,"t":token,"blendTargets":[{"component":compA,"attractor":{"point":vecA,"range":rangeA}},{"component":compB,"attractor":{"point":vecB,"range":rangeB}}]}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

# def twoSurfaceLattice_attractor(component,base,ceil,cellHeight,autoScale,filename,compA,vecA,rangeA):
#
#     url = "https://studiobitonti.appspot.com/surfaceLattice"
#     payload = {"component":component,"base":base,"autoScale:autoScale,""ceil":ceil,"cellHeight":cellHeight,"filename":filename,"t":token,"blendTargets":[{"component":compA,"attractor":{"point":vecA,"range":rangeA}}]}
#     print(json.dumps(payload))
#     r = requests.post(url,json=payload)
#     return r.text

class surfaceLattice:
    def __init__(self): #set global variables
        #URL is always this.
        self.url = "https://studiobitonti.appspot.com/surfaceLattice"
        #Always True
        self.autoScale="true"

        self.output = "twoSurfaceLattice_attractor_output.obj"
        self.cellHeight=1
        #attactors will be formated as an 2D array "["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]"
        #default values are files included in sample repo.
        self.attractorSet=[["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]
        self.component="unit_1.obj"
        self.base="Base_Surface.obj"
        self.ceil="Ciel_CompB"

#functions for seting key variables

    def setAttractor(self,a): #attractors are optional (blended lattices only)
        self.attractorSet=a
    def setOutput(self,output):#file name that you want to save out
        self.output=output
    def setSurface(self,base):#base surface
        self.base=base
    def setTopSurface(self,ceil):#Top surface
        self.ceil=ceil
    def setCellHeight(self,cellHeight):#if no top surface is defined set a cell height. Else it will be set to 1
        self.cellHeight=cellHeight

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

    def surfaceLatticeOffset(self):
        payload = {"component":self.component,"base":self.base,"cellHeight":self.cellHeight,"filename":self.output,"t":token}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        return r.text

def marchingCube(lines,resolution,memberThickness,filename):

    url = "https://studiobitonti.appspot.com/marchingCube"
    payload = {"lines":lines,"resolution":resolution,"memberThickness":memberThickness,"filename":filename,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text
