pwd1 = 'myPass'
pwd2 = 'myPass'

#Todo:Write the password logic using if..else condtional statements and print the output below.


if pwd1 == pwd2:
    print("Password Changed")
else:
    if pwd1.casefold() == pwd2.casefold():
        print("Password Doesn't Match, Check Case")
    else:
        print("Password Doesn't Match")