# create a function is_palindrome(word) return true if the word is palindrome string else return false
# using sliceing


def is_palindrome(word):
    reverse_str=word[::-1]
    if word==reverse_str:
        return True
    return False
print(is_palindrome("malayalam"))


# def is_palindrome(word):
#   reversed+str=word[::-1]
#    return word==reversed_str
# print(is_palindrome(malayalam))