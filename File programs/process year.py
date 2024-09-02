

f_read=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\File programs\\years.txt","r")
f_century=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\File programs\\century_years.txt","w")
f_non_century=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\File programs\\non_century_years.txt","w")

for year in f_read:
    y=int(year.rstrip("\n"))
    if y%100==0:
        f_century.write(str(y)+"\n")
    else:
        f_non_century.write(str(y)+"\n")  