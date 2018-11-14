import requests
import json

def stochasticLattice(volume,poreSize,filename,t):

    url = "https://studiobitonti.appspot.com/stochasticLattice"
    payload = {"volume":volume,"poreSize":poreSize,"filename":filename,"t":t}
    r = requests.post(url,json=payload)
    return r.text

def volumeLattice(component,volume,componentSize,filename,t):

    url = "https://studiobitonti.appspot.com/volumeLattice"
    payload = {"component":component,"volume":volume,"componentSize":componentSize,"filename":filename,"t":t}
    r = requests.post(url,json=payload)
    return r.text

def volumeLattice_attractor(component,volume,componentSize,filename,t):

    url = "https://studiobitonti.appspot.com/volumeLattice"
    payload = {"component":component,"volume":volume,"componentSize":componentSize,"filename":filename,"t":t,"blendTargets":[{"component":"unit_0.obj","attractor":{"point":[0,0,0],"range":2}}]}
    r = requests.post(url,json=payload)
    return r.text
