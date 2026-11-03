sentence = "Python is easy to learn"
word=sentence.split()
reversed_sentence=""
for ch in word:
    reversed_sentence=ch + " " +reversed_sentence
print(reversed_sentence.strip())
