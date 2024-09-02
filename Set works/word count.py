# print the word count

words=["hello","hai","hello","hai","hai","hi"]

# words_set=set(words)
# for w in words_set:
#     print(w,words.count(w))


word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)