text = "abde"
for i in range(len(text)-1):
    if ord(text[i+1]) - ord(text[i])>1:
        print(chr(ord(text[i])+1))
        break
