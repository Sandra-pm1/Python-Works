# read height and weight frm the user and calculate BMI
# print under weight if BMI<19
# print normal weight if BMI in range of 19-25
# print over weight if BMI in range of 25-30
# print obesity 

weight_in_kg=int(input("Enter the weight "))
height_in_cm=int(input("Enter the height "))

height_in_meter=height_in_cm/100
bmi=weight_in_kg/height_in_meter**2
print(f"bmi of a person with height {height_in_cm} and weight {weight_in_kg} = {bmi}")

if bmi<19:
    print("Under weight")
elif bmi<=25:
    print("Normal weight")
elif bmi<=30:
    print("Over weight")
else:
    print("Obesity")
