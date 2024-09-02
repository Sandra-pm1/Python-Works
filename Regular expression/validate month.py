

# validate month
# (01,02,03,04,05,06,07,08,09,10,11,12)


from re import fullmatch
month=input("Enter a month : ")

pattern="(0?[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)
print("Invalid" if matcher==None else "Valid")