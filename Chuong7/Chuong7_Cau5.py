import json
pythonObject = {
 "ten": "Tran Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}
jsonString = json.dumps(pythonObject)
print(jsonString)