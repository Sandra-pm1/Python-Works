
# variable name
# first charcter must be an alphabet k to m
# second letter must be a number that is / 3
# followed by any number r alphabets and numbers


from re import fullmatch
variable_name=input("Enter variable name : ")

pattern="[k-mK-M][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,variable_name)
print("invalid" if matcher==None else "valid")