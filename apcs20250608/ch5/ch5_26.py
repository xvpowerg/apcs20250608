poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉
'''
try:
    file = open("output3.txt","w")
    file.write(poem)
except Exception as ex:
    print("ex:",ex)
finally:
    file.close()
