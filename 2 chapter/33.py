import re 
password = input("Enter password: ")
l = 0
if len(password) >= 8:
    for i in password:
        if re.search("[AZ]", password):
            l+=1 

        if re.search("[az]", password):
            l+=1

        if re.search("[0-9]", password):
            l+=1

        if re.search("[!@#$%^&*()-+]", password):
            l+=1 

        if re.search("\s", password): 
            l+=1

if (l>=4 and len(password) >= 8):
    print('valid password')

else:
    print('invalid password')
