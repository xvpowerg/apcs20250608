from calculator import calcBmi
h = int(input("身高:"))
w = int(input("體重:"))
bmi = calcBmi(h,w)
print(f"{bmi:.2f}")
