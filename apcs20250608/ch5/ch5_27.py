poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉
'''
try:
  with open("output4.txt","w") as f:
      f.write(poem)
except Exception as e:
    print("錯誤:",e)
