
from re import findall

text="the fat cat run fast to catch the rat"

pattern=".at"

matcher=findall(pattern,text)

print(matcher)