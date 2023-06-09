# ........FOR THE REGEX(REGULAR EXPRESSION)..........

import re
import mysql.connector

# ...........CREATING DATABASE.....................

mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE GUNREGISTER")

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="GUNREGISTER"
)

mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

mycursor.execute("CREATE TABLE REGISTER (NAME VARCHAR(255), AGE INT, GUN_TYPE VARCHAR(255), GUN_REG_NUMBER INT PRIMARY KEY)")

#...................TO ALTER TABLE.................

# mycursor.execute("ALTER TABLE REGISTER

# ...........INPUTING INTO DATABASE....................
def gun_reg_validation(name,age ,user,gun_reg_num):
    while True:
        gun_reg_num = input("Enter Gun Registeration Number: ")
        pattern='[a-zA-Z]{3}[0-9]{5}[a-zA-Z]{2}$'
        match= re.search(pattern,gun_reg_num)
        if match:
            print("GUN REGISTERATION NUMBER IS VALID!")
            #............ INSERTING INTO GUNREGISTER DATABASE TABLE REGISTER ...........

            inputtingvalues(name,age ,user,gun_reg_num)
            break

        else:
            print("GUN REGISTERATION NUMBER IS INVALID!")
            continue

def inputtingvalues(name,age ,user,gun_reg_num):

    sql = "INSERT INTO REGISTER (NAME,AGE,GUN_TYPE,GUN_REG_NUMBER ) VALUES (%s, %s, %s, %s)"
    val = (name,age ,user,gun_reg_num)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

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
        guns=["ASSAULT",  "SNIPER" , "SMG" , "PISTOL" , "MARKSMAN", "SHOTGUN", "LMG"]
        
        while True:
            user=input("ENTER CATEGORY: ").upper()
            if user==guns[1]:
                print("\nAK47 KILO141 "
                      "M4   M16 "
                      "AK117    FFAR15  "
                      "ASVAL    PEACEKEEPERMK2  "
                      "KRIG6    ODEN\n")
                gun_reg_num=""

                # .........CALLING THE GUN VALIDATION FUNCTION..........
                gun_reg_validation(name,age ,user,gun_reg_num)
                
                break
            else:
                print("SELECT A VALID CATEGORY!")



user_reg()


