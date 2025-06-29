## BMI 計算函式 作業


##bmi 公式寫成函式
def calcBMI(h,w):
    return w / ((h/100)**2)
#bmi狀態寫成函示
def diagnose(bmi):
    result = "錯誤的數值"
    if bmi > 30:
        result = "胖胖"
    elif bmi > 25:
        result = "過重"
    elif bmi > 18.5:
        result = "正常"
    elif bmi > 0:
        result = "過輕"
    return result

h = float(input("身高"))
w = int(input("體重"))
bmi = calcBMI(h,w)
msg = diagnose(bmi)
print(f"bmi:{bmi:.2f} {msg}")
