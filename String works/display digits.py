# print digit in the string

word="i have 2 bikes and 1 car"

for ch in word:
    if ch.isdigit():
        print(ch,end=" ")
    

# print alphabets in the string

print()
for ch in word:
    if ch.isalpha():
        print(ch,end=" ")