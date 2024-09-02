

from re import finditer

text="abc 7klegf@#"

# pattern="\d"    # [0-9]
# pattern="\D"    # [^0-9]
# pattern="\w"    # [a-zA-Z0-9]
# pattern="\W"    # [^a-zA-Z0-9]
# pattern="\s"    # space
pattern="\S"      # exclude space

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"===",m.group())


# + match one or more
# ? optional
# * zero or more
# . any