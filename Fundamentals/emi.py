#program to calculate emi

#loan amt
#interest
#loan tenure

loan_amnt=5000000
intrest=9/12/100
loan_tenure=20*12

emi=loan_amnt*intrest*(1+intrest)**loan_tenure/((1+intrest)**loan_tenure-1)
total_amnt=emi*loan_tenure
total_intrest=(total_amnt-loan_amnt)  

print(f"EMI={emi}")
print(f"Total payable amount={total_amnt}")
print(f"Total intrest={total_intrest}")

# 0.0075(loan_amnt)
# 240(loan_tenure)
   