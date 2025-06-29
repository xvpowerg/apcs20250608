#英文單字出現次數
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
myDict = {}
songLower = song.lower()
for ch in song:
    if ch in ".,?":
        songLower = songLower.replace(ch,"")
print(songLower)

songSplit =  songLower.split()
for wd in songSplit:
    if wd in myDict:
        myDict[wd] += 1
    else:
        myDict[wd] = 1
print(myDict)        
