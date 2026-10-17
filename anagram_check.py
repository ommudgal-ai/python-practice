text1 = "listen"
text2 = "silent"
freq1={}
freq2={}
for ch in text1:
    if ch not in freq1:
        freq1[ch]=1
    else:
        freq1[ch]+=1
for ch in text2:
    if ch not in freq2:
        freq2[ch]=1
    else:
        freq2[ch]+=1
if freq1==freq2:
    print("Anagrams")
else:
    print("not Anagrams")
