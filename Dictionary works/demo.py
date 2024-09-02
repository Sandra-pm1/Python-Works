

# student={"name":"sandra","course":"django"}
# for i in student:
#    print(student[i])

# # update the course as full stack in student

# for i in student:
#     if i=="course":
#         student[i]="fullstack"
# print(student[i])


# create a dictionary mobile with keys name,brnd,price,is_available

mobile={"name":"motoedge14","brand":"moto","price":22000,"is_available":True}

# print mobile name

print(mobile.get("name"))
for k,v in mobile.items():
    print(k,v)

# add a key:value to dictionary offer:500

mobile["offer"]=500
print(mobile)

# selling price

if offer in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")
    print(selling_price)
else:
    selling_price=mobile.get("price")
    print(selling_price)
