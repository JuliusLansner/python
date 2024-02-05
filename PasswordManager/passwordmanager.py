master_pwd = input("What is the master password?")

def view():
    with open('passwordstest.txt','r') as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('passwordstest.txt','a') as f:
        f.write(name + "|" + pwd +"\n")
        
while True:
    mode = input("add new or view existing passwords? (add, view or q to quit)")
    if mode == "q":
        break
    
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("invalid mode")