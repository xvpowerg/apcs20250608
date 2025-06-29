scores = {"Ch":100,"En":80,"Ma":95}

for k in scores.keys():
    print(k,scores[k],end=" ")

print()

for k in scores:
    print(k,scores[k],end=" ")
print()

for k,v in scores.items():
    print(k,v,end=" ")
print()    
print("="*50)
print(scores["En"])
#print(scores["OS"])
print(scores.get("Ma"))
print(scores.get("OS"))
print("End")
