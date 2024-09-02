
# first character must be alphabet
# followed by any alphabet,digit or _


from re import fullmatch

variable_name=input("Enter variable name : ")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,variable_name)
print("Invalid" if matcher==None else "Valid")