text = "banana"
frequency={}
value=0
char=None
for ch in text:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
for ch in frequency:
    if frequency[ch]>value:
        value=frequency[ch]
        char=ch
print(char)
