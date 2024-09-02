
# validate mobile number with country code mandatory
# 10 digits
# number starts with 6,7,8,9


from re import fullmatch
mobile_number=input("Enter mobile number : ")

pattern="(91)\s?[6-9]\d{9}"

matcher=fullmatch(pattern,mobile_number)
print("Invalid" if matcher==None else "Valid")
