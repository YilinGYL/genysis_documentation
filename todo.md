MarchingCube Preview flag generates error when set to true

{"memberThickness": 1, "lines": "lattice_example.obj", "filename": "shoe", "t": "dev", "preview": "true", "resolution": 500}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "genysis/genysis.py", line 243, in marchingCube
    return parseResponse(r,printResult=True)
  File "genysis/genysis.py", line 15, in parseResponse
    raise RuntimeError(r.text)
RuntimeError: {"error_status":500,"error_message":"","error":{}}

genLatticeUnit is still an issue when all the values are 0
genysis.genLatticeUnit(7,0.0,0.0,0.0,0.0,1.0,cellName,token)

RuntimeError: {"error_status":500,"error_message":"missing input filed: \"chamfer\", input type: float from 0.0 to 1.0\nmissing input filed: \"centerChamfer\", input type: float from 0.0 to 1.0\nmissing input filed: \"bendIn\", input type: float from 0.0 to 1.0\nmissing input filed: \"cBendIn\", input type: float from 0.0 to 1.0\n","error":{}}
