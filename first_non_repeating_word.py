words = ["apple", "banana", "apple", "mango", "banana", "orange"]
freq={}
for ch in words:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for ch in freq:
    if freq[ch]==1:
        print(ch)
        break
