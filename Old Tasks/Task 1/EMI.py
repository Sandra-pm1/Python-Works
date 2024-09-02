# write a pgrm to calculate
# monthly emi
# total payment
# total interest
# read loan amount,tenure,interest_rate frm the user


loan_amnt=int(input("Enter the loan amount "))
anual_interest=int(input("Enter the interest rate "))
anual_tenure=int(input("Enter the loan tenure "))

interest=int(anual_interest)/12/100
loan_tenure=anual_tenure*12

emi=loan_amnt*interest*(1+interest)**loan_tenure/((1+interest)**loan_tenure-1)
total_amnt=emi*loan_tenure
total_interest=(total_amnt-loan_amnt)    

print(f"EMI={emi}")
print(f"Total payable amount={total_amnt}")
print(f"Total interest={total_interest}")
