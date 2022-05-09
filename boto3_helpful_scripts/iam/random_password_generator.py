from random import choice

len_of_password=8
valid_char='abcdefghijklmnopqrstyuwxz!@#$%^&()?'

pas=[]
for char in range(len_of_password):
    pas.append(choice(valid_char))

password=''.join(pas)
print(password)

ran_pass = ''.join(choice(valid_char) for char in range(len_of_password))
print(ran_pass)