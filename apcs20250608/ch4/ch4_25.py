scores = [70,80,25,76,83,94,51]
name =   ["ken","vivin","ken","lucy","lucy","vivin","ken"]
myDict = {}

for k,v in zip(name,scores):
    if k in myDict:
        myDict[k] += v
    else:
        myDict[k] = v
for k,v in myDict.items():
    print(k,":",v)
    
