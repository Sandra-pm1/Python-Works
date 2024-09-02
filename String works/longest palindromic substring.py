  # longest palindromic substring frm givn string

text="RACECAR"
longest_palindrome=""
length=len(text)
for i in range(0,length):
     left=i
     right=i
     while(left>=0 and right<length and text[left]==text[right]):
        curent_palindrome=text[left:right+1]
        if len(curent_palindrome)>len(longest_palindrome):
            longest_palindrome=curent_palindrome
        left=left-1
        right=right+1
print(longest_palindrome)
