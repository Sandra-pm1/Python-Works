# validate pan card number
# first 3 characters are alphabets
# 4th place PCAHFT
# 5th place alphabet
# 4 digits
# 1 alphabet


from re import fullmatch
pan_num=input("Enter pan card number : ")

pattern="[A-Z]{3}[PCAHFT][A-Z]\d{4}[A-Z]"

matcher=fullmatch(pattern,pan_num)
print("Invalid" if matcher==None else "Valid")