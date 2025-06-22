def c2f(c=10):
    f = 9 / 5 * c + 32
    return f
while True:
    inStr = input("輸入攝氏溫度(q離開)")
    if inStr == 'q':
        print("完成")
        break
    tc = float(inStr)
    tc = c2f(tc)
    print(f"攝氏:{inStr} 華氏:{tc:.2f}")
