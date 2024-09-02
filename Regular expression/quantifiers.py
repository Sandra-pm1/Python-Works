from re import finditer
text="abc123 edf456#@fg987pqr"
pattern="([a-z]{3}|[0-9]{3})"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"===",m.group())
    