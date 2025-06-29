scores = {"Ch":100,"En":80,"Ma":95}
scores["En"] = 99
print(scores)
scores["Os"] = 75
print(scores)

data= {"Ma":96}
scores.update(data)
print(scores)
data = {"Os":88,"La":25,"Ch":71}
scores.update(data)
print(scores)



