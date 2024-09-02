# merge two strings

# case 1
# word1="PQRS"
# word2="ABCD"
# output=PAQBRCSD

word1="PQRS"
word2="ABCD"
merged_string=""
for i in range(0,len(word1)):
    merged_string=merged_string+word1[i]+word2[i]
print(merged_string)
