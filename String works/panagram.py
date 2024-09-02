# check the text is panagram

text="The quick brown fox jumps over the lazy dog"
text=text.lower()
alphabets="abcdefghijklmnopqrstuvwxyz"
is_panagram=True
for ch in alphabets:
    if text.count(ch)==0:
        is_panagram=False 
        break
print(is_panagram)