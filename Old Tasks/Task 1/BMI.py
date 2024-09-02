# write a pgrm to print bmi
# read height and weight frm the user


weight_in_kg=int(input("Enter the weight "))
height_in_cm=int(input("Enter the height "))

height_in_meter=height_in_cm/100
bmi=weight_in_kg/height_in_meter**2
print(f"bmi of a person with height {height_in_cm} and weight {weight_in_kg} = {bmi}")