text="RACECAR"
longest_palindrome=""
for i in range(0,len(text)):
    left=i
    right=i
    while(left>=0 and right<0 and text[left]==text[righ]):
        current_palindrome=text[left:right+1]
        if len(current_palindrome)>len(longest_palindrome):
            longest_palindrome=current_palindrome
        left=left-1
        right=right+1
print(longest_palindrome)