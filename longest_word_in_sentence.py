sentence = "Python programming is interesting"
words = sentence.split()
word=words[0]
number=len(word)
for ch in words:
    if len(ch)>number:
        word=ch
        number=len(ch)
print(word)
