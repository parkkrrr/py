usr=str(input("Enter Username : "))
passwd=input("Enter Password : ")
attempts=0

while(attempts!=3 and passwd.__len__==8):
    login_usr=str(input("Enter Username :"))
    login_passwd=input("Enter password :")

    if(login_usr==usr and passwd==login_passwd):
        print("Welcome {}".format(login_usr))
        break

    else: print("Permission Denied. Try again")
    attempts+=1

else:
    print("Password Length is short : {}".format(len(passwd)))
