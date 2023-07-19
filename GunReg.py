# ........FOR THE REGEX(REGULAR EXPRESSION)..........

import re
import sqlite3

# # ...........CREATING DATABASE.....................

mydb = sqlite3.connect("GUNREGISTER")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS REGISTER (NAME VARCHAR(255), AGE INT, GUN_TYPE VARCHAR(255), GUN_REG_NUMBER INT PRIMARY KEY)")
mycursor.execute("CREATE TABLE IF NOT EXISTS REGISTERADMIN (NAME VARCHAR(255), AGE INT, PASSCODE INT )")

# INPUTING INTO ADMIN DATABASE
def admintable():
    name=str(input("ENTER ADMIN NAME: ")).upper()
    age=int(input("ENTER ADMIN AGE: "))
    while True:
        passcode=input("ENTER ADMIN PASSWORD: ")
        if len(passcode) <= 5:
            print("PASSWORD TOO WEAK!, LENGHT MUST BE GREATER THAN 5")
            continue
        else:
            break

    sql = "INSERT INTO REGISTERADMIN (NAME,AGE,PASSCODE ) VALUES (?, ?, ?)"
    val = (name,age ,passcode)
        
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
# admintable()






#...................TO ALTER TABLE.................

# mycursor.execute("ALTER TABLE REGISTER



# ...........INPUTING INTO DATABASE....................
def gun_reg_validation(name,age ,gun_types,gun_reg_num):
    while True:
        print("Gun must follow format example: abc12345qw")
        gun_reg_num = input("Enter Gun Registeration Number: ").upper()
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
    print("DATABASE FILEPATH:")
    for row in rows:
        print(row)

def viewdatabase():
    mycursor.execute("SELECT * FROM REGISTER")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def viewing():
        filepath()
        viewdatabase()

# ...............REMOVING GUNS.................

def gundeletion():
    while True:
        choizes=int(input("Would you like to format database or remove one infomation: (format=1 / remove=2 /exit=3) "))
        if choizes==1:
            mycursor.execute("DELETE FROM REGISTER")
            print()
            print(mycursor.rowcount," Deleted")
            mycursor.execute("SELECT * FROM REGISTER")
            print(mycursor.fetchall())
            mydb.commit()
            break
        elif choizes==2:
            print("WHICH GUN WOULD YOU LIKE TO REMOVE")
            while True:
                gun_reg_num = input("Enter Gun Registeration Number: ").casefold()
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
                        print(mycursor.rowcount," record deleted")
                        
                        viewdatabase()
                        break
                else:
                    print("GUN REGISTERATION NUMBER IS INVALID!")
                    continue  

        elif choizes==3:
            break    
        else:
            print("invalid option!")
            continue

        break

    

        


 # .....FINDING WHO GUN IS REGISTERED TO........

def findowner():
    while True:
        gun_reg_num = input("Enter Gun Registeration Number: ").casefold()
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
            print("GUN REGISTERATION NUMBER IS INVALID! OR DOES NOT EXIST IN DATABASE")
            continue

# .......Decision to find and delete............
def decision():
    while True:
        print("\nWELCOME TO THE ADMIN SECTION")
        inpur = input('CONTINUE | <-BACK:').casefold()
        if inpur=="continue":
            while True:
                print('ADMIN NAME AND PASSOWRD REQUIRED')
                inpu=input('ENTER NAME: ').casefold()
                pas =input('ENTER PASSWORD: ')
                mycursor.execute("SELECT * FROM REGISTERADMIN WHERE NAME = ?  AND PASSCODE = ? ", (inpu,pas))
                if mycursor.fetchone() is None:
                    print('USER DOES NOT EXIST!.\tRETRY | <-GO BACK\n')
                    while True:
                        inpurt = input('RETRY | <-BACK TO MAIN MENU:').casefold()
                        if inpurt=="retry":
                            break
                        elif inpurt=="back":
                            break
                        else:
                            print("INVALID INPUT!!")
                        continue

                    if inpurt == "retry":
                        continue
                    elif inpurt == "back":
                        signin()
                        break
                break

            else:
                print("WELCOME",inpu.upper())
                while True:
                    try:
                        chooz=str(input("WOULD YOU LIKE TO REMOVE FROM DATABASE OR CHECK INFO IN DATABASE? (remove / check / viewdb / back) :")).casefold()
                        if chooz=='remove':
                            gundeletion()

                        elif chooz=='check':
                            findowner()

                        elif chooz=='back':
                            signin()
                            break

                        elif chooz=='viewdb':
                            viewing()

                        else:
                            print("INVALID OPTION")
                            continue
                    except ValueError:
                        print("INVALID OPTION")
                        continue
        elif inpur=="back":
            signin()
            break
        else:
            print("INVALID INPUT!!")
            continue
        break



def pickgun(name,age,gun_types,gun_reg_num,guns,gunner,gunt):
    while True:
            while True:
                try:
                    if gunt==1:
                        print("Pick one from 1 -",len(guns['ASSAULT']),"\n")
                    elif gunt==2:
                        print("Pick one from 1-",len(guns["SNIPER"]),"\n")
                    elif gunt==3:
                        print("Pick one from 1-",len(guns["SMG"]),"\n")
                    elif gunt==4:
                        print("Pick one from 1-",len(guns["PISTOL"]),"\n")
                    elif gunt==5:
                        print("Pick one from 1-",len(guns["SHOTGUN"]),"\n")
                    elif gunt==6:
                        print("Pick one from 1-",len(guns["LMG"]),"\n")
                
                    gun_type=int(input("Pick one: "))


                    print("YOU CHOOSE:",guns[gunner][gun_type-1])
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
    

# ............user section.................

def user_reg():
    print("WELCOME TO USER SECTION")
    while True:
        while True:
            try:
                pattern='[a-zA-Z]$'
                name = str(input ("ENTER YOUR NAME: ")).upper()
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
                    pickgun(name,age,"",7,guns,gunner,1)

                    while True:
                        try:
                            choiz=str(input("Would you like to get another gun: (yes / no) ")).casefold()
                            if choiz=='yes':
                                break
                            elif choiz=='no':
                                break
                            else:
                                print("invalid option!")
                                continue
                        except ValueError:
                            print("invalid option!")

                elif user_input==2:
                    gunner="SNIPER"
                    print(guns["SNIPER"])

                    pickgun(name,age,"",7,guns,gunner,2)

                    while True:
                        try:
                            choiz=str(input("Would you like to get another gun: (yes / no) ")).casefold()
                            if choiz=='yes':
                                break
                            elif choiz=='no':
                                break
                            else:
                                print("invalid option!")
                                continue
                        except ValueError:
                            print("invalid option!")

                elif user_input==3:
                    print(guns["SMG"])
                    gunner="SMG"
                    pickgun(name,age,"",7,guns,gunner,3)

                    while True:
                        try:
                            choiz=str(input("Would you like to get another gun: (yes / no) ")).casefold()
                            if choiz=='yes':
                                break
                            elif choiz=='no':
                                break
                            else:
                                print("invalid option!")
                                continue
                        except ValueError:
                            print("invalid option!")

                elif user_input==4:
                    print(guns["PISTOL"])
                    gunner="PISTOL"
                    pickgun(name,age,"",7,guns,gunner,4)

                    while True:
                        try:
                            choiz=str(input("Would you like to get another gun: (yes / no) ")).casefold()
                            if choiz=='yes':
                                break
                            elif choiz=='no':
                                break
                            else:
                                print("invalid option!")
                                continue
                        except ValueError:
                            print("invalid option!")

                elif user_input==5:
                    gunner="SHOTGUN"
                    print(guns["SHOTGUN"])
                    pickgun(name,age,"",7,guns,gunner,5)

                    while True:
                        try:
                            choiz=str(input("Would you like to get another gun: (yes / no) ")).casefold()
                            if choiz=='yes':
                                break
                            elif choiz=='no':
                                break
                            else:
                                print("invalid option!")
                                continue
                        except ValueError:
                            print("invalid option!")

                elif user_input==6:
                    gunner="LMG"
                    print(guns["LMG"])
                    pickgun(name,age,"",7,guns,gunner,6)

                    while True:
                        try:
                            choiz=str(input("Would you like to get another gun: (yes / no) ")).casefold()
                            if choiz=='yes':
                                break
                            elif choiz=='no':
                                break
                            else:
                                print("invalid option!")
                                continue
                        except ValueError:
                            print("invalid option!")
                else:
                    print("SELECT A VALID CATEGORY!")
                    continue
                break
            while True:
                chod=input("ANYBODY ELSE? ").casefold()
                if chod=='yes':
                    break
                elif chod == 'no':
                    break
                else:
                    print("invalid option!")
                    continue
            if chod=='yes':
                continue
            elif chod == 'no':
                break
        break
                


            
#.............admin or user selection section.................
def signin():
    while True:
        print("MAIN MENU")
        use=str(input("ARE YOU A USER OR AN ADMIN? (ADMIN / USER / EXIT) " )).casefold()
        if use=='admin':
            # viewing()
            decision()
            break
        elif use=='user':
            user_reg()
            break
        elif use=='exit':
            break
        else:
            print("INVALID OPTION!")
            continue
signin()

import tkinter


