amount=5000000
anual_interest=9
loan_tenure=20
 
interest=anual_interest/100/12
tenure=loan_tenure*12

emi=amount*interest*(1+interest)**tenure/(1-interest)**tenure-1
total_amount=emi*tenure
total_interest=total_amount-amount