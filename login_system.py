while True:
    print("\n1.register")
    print("2.login")
    print("3.exit")

    choice = input("enter choice: ")

    if choice == "3":
        print("exiting...")
        break

    if choice == "1":
        username = input("enter username: ")
        password = input("enter password: ")

        f = open("user.txt", "a")
        f.write(username + "=" + password + "\n")
        f.close()


        print("register successfully")

    elif choice == "2":
        username = input("enter username: ")
        password = input("enter password: ")

        found = False

        try:
            with open("user.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    u,p = line.split("=")

                    if u == username and p == password:
                        print("login successful")
                        found = True
                        break
        except:
            print("no users found")
        if not found:
            print("invalid username or password")
          
