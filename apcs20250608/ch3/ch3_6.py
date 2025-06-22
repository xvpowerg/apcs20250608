subjs = ['國語', '數學', '英文']
scores = [100, 80, 95]

for i in range(len(subjs)):
    print(f"{subjs[i]} {scores[i]}")


print(list(zip(subjs,scores)))

for n,s in zip(subjs,scores):
    print(n,s)
#輸出
#國語 100
#數學 80
#英文 95
