
f=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\File programs\\news.txt","r")

# word_lst=[]
# for line in f:
#     words=line.rstrip("\n").split(" ")
#     for w in words:
#         word_lst.append(w)
# print(word_lst)

word_lst=[w for line in f for w in line.rstrip("\n").split(" ")]

# word_count={}
# for w in word_lst:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1

word_count={w:word_lst.count(w) for w in word_lst}
# print(word_count)

def get_value(key):
    return word_count.get(key)
srt=sorted(word_count,key=get_value,reverse=True)
print(srt)
