
f=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\File programs\\land slides.txt","r")

data=[]

for line in f:                                                 # Kerala 2018 14
    lst=line.rstrip("\n").split(" ")                           # ["Kerala","2018",14]
    dic={"state":lst[0],"year":lst[1],"death":int(lst[2])}     # {"state":"kerala","year":"2018","death":14}
    data.append(dic)
#print(data)

# find the total death
total_death=sum([dic.get("death")for dic in data])
#print(total_death)

# death per state
death_per_state={}
for dic in data:
    state=dic.get("state")
    death_count=dic.get("death")
    if state in death_per_state:
        death_per_state[state]+=death_count
    else:
        death_per_state[state]=death_count
#print(death_per_state)

# state with highest death in a year
for dic in data:
    highest_death=max([dic.get("death")for dic in data])
    highest_death_state=[dic.get("state") for dic in data if dic.get("death")==highest_death]
print(highest_death_state)
