from re import fullmatch

f_read=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\Regular expression\\register number.txt","r")
f_write=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\Regular expression\\valid register number.txt","w")

for reg in f_read:

    valid_num=reg.rstrip("\n")

    pattern="(KL)\s?\d{2}\s?[A-Z]{1,2}\s?\d{4}"

    matcher=fullmatch(pattern,valid_num)

    if matcher!=None:

        f_write.write(valid_num+"\n")