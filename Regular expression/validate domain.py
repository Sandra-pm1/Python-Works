from re import fullmatch
f=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\Regular expression\\domain.txt","r")

pattern="[\w\W]+\\.com"

for line in f:
    domain=line.rstrip("\n")
    matcher=fullmatch(pattern,domain)
    if matcher!=None:
        print(domain)
