num1=100

num2=200

print(f"Before swapping num1={num1} num2={num2}")

#logic1(temp variable)

#temp=num1

#num1=num2

#num2=temp

#logic2(adding and subtracting)

#num2=num2-num1

#num1=num1+num2

#logic3(using coma)

#num1,num2=num2,num1

#logic4(using xor)

num1=num1^num2
num2=num1^num2
num1=num1^num2

print(f"After swapping num1={num1} num2={num2}")   