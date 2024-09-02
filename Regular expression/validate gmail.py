# validate gmail id
# starts with alphabet



from re import fullmatch
gmail_id=input("Enter gmail id : ")
 
pattern="\\w[\\w\\._]*@gmail.com"

matcher=fullmatch(pattern,gmail_id)
print("Invalid" if matcher==None else "Valid")
