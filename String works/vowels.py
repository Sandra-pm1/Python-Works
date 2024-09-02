# find the count of vowels in the given text

text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels="aeiou"

# count=0
# for ch in text:
#     if vowels.count(ch)!=0:
#         count=count+1
# print(count)

# consonants_count

count=0
for ch in text:
    if vowels.count(ch)==0:
        count+=1
print(count)
