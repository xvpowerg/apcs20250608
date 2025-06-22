result = {"David":0,"Amy":0,"Sean":0}
nameList = {"David","Amy","Sean"}
for i in range(5):
    vote = input("投票給:")
    if vote not in nameList:
        print("無效票")
        continue
    result[vote]+=1
print(result)
