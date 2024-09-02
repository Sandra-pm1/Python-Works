# first character upper case alphabet
# next character from 1-9
# digit 0-9
# 0 or space
# 4 digit 0-9
# digit 1-9


from re import fullmatch
passport_num=input("Enter passport number : ")

pattern="[A-Z][1-9]\d[0|\\s]\d{4}[1-9]"

matcher=fullmatch(pattern,passport_num)
print("Invalid" if matcher==None else "Valid")