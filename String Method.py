message = "I am a good boy in my class of all the boys"
count = message.find("good boy")
print (count)
text_count= message.count('good boy')
print(text_count)
public=message.replace('boy', 'girl')
print (public)
message = message.capitalize()
print(message)
message = message.upper()
print(message)

table=str.maketrans('abcdef', 'uvwxyz')
fad='fad'.translate(table)
print(fad)
