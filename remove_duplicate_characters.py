text = "programming"
set=[]
new=""
for ch in text:
    if ch not in set:
        set.append(ch)
        new=new+ch
print(new)
