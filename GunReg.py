import re

# ...............................CREATING DATABASE..........................................

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"

)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#...................TO ALTER TABLE.................

# mycursor.execute("ALTER TABLE customers

# ............................................INPUTING INTO DATABASE...........................................

def gun_reg_validation():
    gun_reg_num = input("Enter Gun Registeration Number: ")
    pattern='[a-zA-Z]{3}[0-9]{5}[a-zA-Z]{2}$'
    match= re.search(pattern,gun_reg_num)
    if match:
        print("GUN REGISTERATION NUMBER IS VALID!")

    else:
        print("GUN REGISTERATION NUMBER IS INVALID!")

# gun_reg_validation()

def user_reg():
    while True:
        try:
            pattern='[a-zA-Z]$'
            name = input ("ENTER YOUR NAME: ")
            match = re.search(pattern, name)
            if match:
                age = int(input("ENTER YOU AGE: "))
                break
            else:
                raise ValueError

        except ValueError:
            print("Enter Correct Value")
            continue
    if age<20:
        print("YOU ARE NOT ELIGIBLE FOR A GUN! ")
    else:
        print("PROCEED WITH THE REGISTRATION!")

        print("WHICH TYPE OF GUN DO YOU WANT "+name.upper()+"\n"
              "{ASSAULT  SNIPER  SMG  PISTOL  MARKSMAN  SHOTGUN  LMG}")
        
        while True:
            user=input("ENTER CATEGORY: ").upper()
            if user=="ASSAULT":
                print("\nAK47 KILO141 "
                      "M4   M16 "
                      "AK117    FFAR15  "
                      "ASVAL    PEACEKEEPERMK2  "
                      "KRIG6    ODEN\n")
                break
            else:
                print("SELECT A VALID CATEGORY!")


# user_reg()


