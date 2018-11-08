import requests

def marchingCubes(lines,resolution,memberThickness,filename,t):

    url = ('https://studiobitonti.appspot.com/marchingCube?lines=%s&resolution=%s&memberThickness=%s&filename=%s&t=%s&wait=true'% (lines,resolution,memberThickness,filename,t))
    ret = requests.get(url)
    print(ret.text)
    return url
