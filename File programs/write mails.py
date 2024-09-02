

f=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\File programs\\mails.txt","w")

mails=[
        "abhi@gmail.com",
        "binu@gmail.com",
        "jinu@gmail.com",
        "sam@gmail.com",
        "vinu@gmail.com"
        ]

for mail in mails:

    f.write(mail+"\n")
