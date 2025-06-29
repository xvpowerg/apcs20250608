## Lambda函式練習
#攝氏溫度轉換華氏溫度程式
cels = [0,10,20,30,40,50,60,70,80,90,100]
fshs = list(map(lambda x:9/5*x+32,cels))
print(fshs)
for c,fs in zip(cels,fshs):
    print(f"攝氏{c}等於華氏{fs:.2f}度")
#9/5*x+32

