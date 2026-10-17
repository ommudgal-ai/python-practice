text = "Data Science"
new=text.lower()
frequency={}
for ch in new:
    if ch in frequency:
        frequency[ch]+=1
    elif ch==" ":
        continue
    else:
        frequency[ch]=1
print(frequency)
