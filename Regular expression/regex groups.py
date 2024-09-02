from re import finditer

text="abc123 @K,7LMdef6"

# pattern="[abf]"                # check for either a,b or f
# pattern="[a-z]"                # check for alphabets from a to z(lower case)
# pattern="[A-Z]"                # check for alphabets from A to z(upper case)
# pattern="[a-zA-Z]"             # check for alphabets both lower and upper case
# pattern="[0-9]" or "\d"        # check for all numbers
# pattern="[a-zA-Z0-9]"          # check for all aplabets(lower and upper cases) and numbers
# pattern="[^a-zA-Z0-9]"         # check for all symbols
# pattern="[^0-9]" or "\D"       # check for all symbols and alphabets
# pattern="[\s]"                 # check for space
pattern="[a-zA-Z\s]"             # check all alphabets(u and l) and space

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"===",m.group())