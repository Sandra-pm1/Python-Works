
# kerala vehicle registraction number validation
# starts with KL
# two digits
# alphabets one or two
# four digits


from re import fullmatch
vehicle_number=input("Enter vehicle number : ")        # KL-47-BN-9876

pattern="(KL)(-)?\d{2}(-)?[A-Z]{1,2}(-)?\d{4}"

matcher=fullmatch(pattern,vehicle_number)
print("Invalid" if matcher==None else "Valid")
