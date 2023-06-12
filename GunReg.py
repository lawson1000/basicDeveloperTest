# ........FOR THE REGEX(REGULAR EXPRESSION)..........

import re
import sqlite3

# # ...........CREATING DATABASE.....................

mydb = sqlite3.connect("GUNREGISTER")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS REGISTER (NAME VARCHAR(255), AGE INT, GUN_TYPE VARCHAR(255), GUN_REG_NUMBER INT PRIMARY KEY)")


#...................TO ALTER TABLE OR DROP.................

# mycursor.execute("DROP TABLE IF EXISTS REGISTER")

# mycursor.execute("ALTER TABLE REGISTER

# ...........INPUTING INTO DATABASE....................
def gun_reg_validation(name,age ,gun_types,gun_reg_num):
    while True:
        gun_reg_num = input("Enter Gun Registeration Number: ")
        pattern='[a-zA-Z]{3}[0-9]{5}[a-zA-Z]{2}$'
        match= re.search(pattern,gun_reg_num)
        if match:
            print("GUN REGISTERATION NUMBER IS VALID!")
            #............ INSERTING INTO GUNREGISTER DATABASE TABLE REGISTER ...........
            mycursor.execute("SELECT * FROM REGISTER WHERE GUN_REG_NUMBER = ?", (gun_reg_num,))
            if mycursor.fetchone() is None:
                print('ID does not exist in the database.')
                inputtingvalues(name,age ,gun_types,gun_reg_num)
                break
            
            else:
                print("ID EXISTIND IN DATABASE!!\nCHECK REGISTERATION NUMBER AGAIN!")
                continue
        else:
            print("GUN REGISTERATION NUMBER IS INVALID!")
            continue

def inputtingvalues(name,age ,gun_type,gun_reg_num):
    sql = "INSERT INTO REGISTER (NAME,AGE,GUN_TYPE,GUN_REG_NUMBER ) VALUES (?, ?, ?, ?)"
    val = (name,age ,gun_type,gun_reg_num)
    
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# ......PRINTING OUT VALUES IN MY DATABASE.........

def filepath():
    mycursor.execute("PRAGMA database_list")
    rows = mycursor.fetchall()
    for row in rows:
        print(row[2])

def viewdatabase():
    mycursor.execute("SELECT * FROM REGISTER")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def viewing(age):
    if age < 20:
        print()   
    else:
        filepath()
        viewdatabase()

# ...............REMOVING GUNS.................

def gundeletion():
    print("WHICH GUN WOULD YOU LIKE TO REMOVE")
    while True:
        gun_reg_num = input("Enter Gun Registeration Number: ")
        pattern='[a-zA-Z]{3}[0-9]{5}[a-zA-Z]{2}$'
        match= re.search(pattern,gun_reg_num)
        if match:
            print("GUN REGISTERATION NUMBER IS VALID!")

            #............ DELETING FROM GUNREGISTER DATABASE TABLE REGISTER ...........
            mycursor.execute("SELECT * FROM REGISTER WHERE GUN_REG_NUMBER = ?", (gun_reg_num,))
            if mycursor.fetchone() is None:
                print('ID does not exist in the database.')
                continue
            
            else:
                print("ID EXISTING IN DATABASE!!\n")
                mycursor.execute("DELETE FROM REGISTER WHERE GUN_REG_NUMBER = ?", (gun_reg_num,)) 
                mydb.commit()
                
                viewdatabase()
                
                break

        else:
            print("GUN REGISTERATION NUMBER IS INVALID!")
            continue


 # .....FINDING WHO GUN IS REGISTERED TO........

def findowner():
    while True:
        gun_reg_num = input("Enter Gun Registeration Number: ")
        pattern='[a-zA-Z]{3}[0-9]{5}[a-zA-Z]{2}$'
        match= re.search(pattern,gun_reg_num)
        if match:
            print("GUN REGISTERATION NUMBER IS VALID!")
            

            mycursor.execute("SELECT * FROM REGISTER WHERE  GUN_REG_NUMBER = ?", (gun_reg_num,))

            myresult1 = mycursor.fetchall()
            for x in myresult1:
                print(x)

            break

        else:
            print("GUN REGISTERATION NUMBER IS INVALID!")
            continue

# .......Decision to find and delete............
def decision(age):
    if age < 20:
        print("REGISTERATION ENDED") 

    else:
        while True:
            
            
            choice=input("WOULD YOU LIKE TO REMOVE GUN REGISTERATION INFO: ")
            if choice=='yes':
                gundeletion()

            elif choice=='no':
                print('....CLOSED')
                break

            else:
                print("INVALID OPTION")
                continue

        while True:

            
            choice=input("WOULD YOU LIKE TO CHECK GUN REGISTERATION INFO: ")
            if choice=='yes':
                findowner()

            elif choice=='no':
                print('Good Bye')
                break

            else:
                print("INVALID OPTION")
                continue



def pickgun(name,age,gun_types,gun_reg_num,guns,gunner):
    while True:
            while True:
                try:
                    gun_type=int(input("Pick one: "))

                    print(guns[gunner][gun_type-1])
                    break
                except IndexError:
                    print("NOT AN OPTION. TRY AGAIN!")
                    continue
                except ValueError:
                    print("NOT AN OPTION. TRY AGAIN!")
                    continue

            for i in guns["ASSAULT"]:                    
                if guns["ASSAULT"][gun_type-1]:
                    gun_types=guns["ASSAULT"][gun_type-1]
                    print("GO FOR REGISTERATION!")
                    # .........CALLING THE GUN VALIDATION FUNCTION..........
                    gun_reg_num=""
                    gun_reg_validation(name,age ,gun_types,gun_reg_num)
                    break
                elif guns["SNIPER"][gun_type-1]:
                    gun_types=guns["SNIPER"][gun_type-1]
                    print("GO FOR REGISTERATION!")
                    # .........CALLING THE GUN VALIDATION FUNCTION..........
                    gun_reg_num=""
                    gun_reg_validation(name,age ,gun_types,gun_reg_num)
                    break
                elif guns["SMG"][gun_type-1]:
                    gun_types=guns["SMG"][gun_type-1]
                    print("GO FOR REGISTERATION!")
                    # .........CALLING THE GUN VALIDATION FUNCTION..........
                    gun_reg_num=""
                    gun_reg_validation(name,age ,gun_types,gun_reg_num)
                    break
                elif guns["PISTOL"][gun_type-1]:
                    gun_types=guns["PISTOL"][gun_type-1]
                    print("GO FOR REGISTERATION!")
                    # .........CALLING THE GUN VALIDATION FUNCTION..........
                    gun_reg_num=""
                    gun_reg_validation(name,age ,gun_types,gun_reg_num)
                    break
                elif guns["SHOTGUN"][gun_type-1]:
                    gun_types=guns["SHOTGUN"][gun_type-1]
                    print("GO FOR REGISTERATION!")
                     # .........CALLING THE GUN VALIDATION FUNCTION..........
                    gun_reg_num=""
                    gun_reg_validation(name,age ,gun_types,gun_reg_num)
                    break
                elif guns["LMG"][gun_type-1]:
                    gun_types=guns["LMG"][gun_type-1]
                    print("GO FOR REGISTERATION!")
                    # .........CALLING THE GUN VALIDATION FUNCTION..........
                    gun_reg_num=""
                    gun_reg_validation(name,age ,gun_types,gun_reg_num)
                    break
                else:
                    print("INVALID CHOICE!")
                    continue
            break

def user_reg():
    while True:
        try:
            pattern='[a-zA-Z]$'
            name = input ("ENTER YOUR NAME: ")
            match = re.search(pattern, name)
            if match:
                age = int(input("ENTER YOU AGE: "))
                ages=age
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

        guns = {"ASSAULT": ["AK47", "KILO141", "M4", "M16", "AK117", "FFAR15", "ASVAL", "PEACEKEEPERMK2", "KRIG6", "ODEN"],
                "SNIPER": ["The Omega", "Voice of Reason", "Sniper Kin", "Fair Looker", "Sharpshooter Sort", "With Intent", "Night Fall", "The Assassin"],
                "SMG": ["MSMC", "AKS-74U (RUS-79U)", "Chicom", "HG40", "PDW-57", "Razorback", "Pharo", "GKS"],
                "PISTOL": ["ALFA Defender", "Deer gun", "Davis Warner Infallible", "Dan Wesson", "2mm Kolibri", "Barrett"],
                "SHOTGUN": ["Lupus Heirloom Of Giants", "Man-O-War", "Midnight", "Loyal Blaster", "Sten"],
                "LMG": ["7,62 ITKK 31 VKT ", "HP 7.62 ",  "AA-52"]
                }
    
        while True: 
            gun_type=0
            
            while True:
                try:
                    print("ASSAULT=1  SNIPER=2  SMG=3  PISTOL=4  SHOTGUN=5  LMG=6")
                    user_input = int( input("ENTER CATEGORY FROM THE OPTIONS PROVIDED: "))
                    break
                
                except ValueError:
                    print("INVALID CHOICE!")
                    continue

            if user_input==1:
                gunner="ASSAULT"
                print(guns["ASSAULT"])
                pickgun(name,age,"",7,guns,gunner)

                while True:
                    choiz=int(input("Would you like to get another gun: (yes=1 / no=2) "))
                    if choiz==1:
                        break
                    elif choiz==2:
                        break
                    else:
                        print("invalid option!")
                        continue

            elif user_input==2:
                gunner="SNIPER"
                print(guns["SNIPER"])

                pickgun(name,age,"",7,guns,gunner)

                while True:
                    choiz=int(input("Would you like to get another gun: (yes=1 / no=2) "))
                    if choiz==1:
                        break
                    elif choiz==2:
                        break
                    else:
                        print("invalid option!")
                        continue

            elif user_input==3:
                print(guns["SMG"])
                gunner="SMG"
                pickgun(name,age,"",7,guns,gunner)

                while True:
                    choiz=int(input("Would you like to get another gun: (yes=1 / no=2) "))
                    if choiz==1:
                        break
                    elif choiz==2:
                        break
                    else:
                        print("invalid option!")
                        continue

            elif user_input==4:
                print(guns["PISTOL"])
                gunner="PISTOL"
                pickgun(name,age,"",7,guns,gunner)

                while True:
                    choiz=int(input("Would you like to get another gun: (yes=1 / no=2) "))
                    if choiz==1:
                        break
                    elif choiz==2:
                        break
                    else:
                        print("invalid option!")
                        continue

            elif user_input==5:
                gunner="SHOTGUN"
                print(guns["SHOTGUN"])
                pickgun(name,age,"",7,guns,gunner)

                while True:
                    choiz=int(input("Would you like to get another gun: (yes=1 / no=2) "))
                    if choiz==1:
                        break
                    elif choiz==2:
                        break
                    else:
                        print("invalid option!")
                        continue

            elif user_input==6:
                gunner="LMG"
                print(guns["LMG"])
                pickgun(name,age,"",7,guns,gunner)

                while True:
                    choiz=int(input("Would you like to get another gun: (yes=1 / no=2) "))
                    if choiz==1:
                        break
                    elif choiz==2:
                        break
                    else:
                        print("invalid option!")
                        continue

            if choiz==1:
                continue
            elif choiz==2:
                viewing(age)
                decision(age)
                break
            


            else:
                print("SELECT A VALID CATEGORY!")
user_reg()



