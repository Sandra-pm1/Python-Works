from re import finditer
text="pythonhellopythonhellohipythonhellohipython"
count=0
matcher=finditer("python",text)
for m in matcher:
    print(m.start(),"====",m.group())
    count+=1
print(count)