
email_id="johnsmith@gmail.com"

# @ index position

at_index_positon=email_id.index("@")

user_name=email_id[:at_index_positon]
mail_id=email_id[at_index_positon:]

print(user_name)  
print(mail_id)