# find the first recursive character frm the list


text="ABCADD"

new_text={}
for ch in text:
    if ch in new_text:
        print(ch)
        break
    else:
        new_text[ch]=1
