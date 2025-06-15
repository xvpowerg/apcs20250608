# 常見跳脫字元
str1 = 'That is Mary\'s car'
print(str1)
str1 = "That is Mary's Car"
print(str1)
str2 = "這是\"Vivin\"的作品 "
print(str2)
str2 = '這是"Vivin"的作品'
print(str2)


msg = '''天文學家利用錢卓望遠鏡和卡爾·央斯基甚大無線電波陣列（VLA）
研究的目標黑洞位在稱為「宇宙正午」\"""的宇宙誕生初期，
也就是大霹靂後約30億年的時期。
過去研究發現在這段時期'的大多數星系和超大質量黑洞，
成長速度比宇宙歷史任何時期都要快。
科學家希望利用黑洞產生的噴流，
探討黑洞在宇宙歷史的這個關鍵時期如何對周圍環境造成影響。'''
print(msg)
