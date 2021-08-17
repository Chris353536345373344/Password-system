def Changercode():
    import random
    var42= random.randint(1000000,9999999)
    f=open ("resetcode.txt", "w+")
    var41 =str(var42)
    f.write(var41)

f=open("pass.txt", "r+")
contents =f.read()

var2 = input("do you want to input your password (y/n) n sets the password ")
if var2 == ("y"):
    var3 =input("what is the password ")
    if var3==(contents):
        print("good job")
        input()


else:
    Changercode()
    f=open("resetcode.txt", "r+")
    content =f.read()

    var4=input("reset code ")
    
    if var4==(content):
        f=open("pass.txt", "w+")
        var1=input("set password ")
        f.write(var1)
        input()
