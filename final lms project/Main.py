import Database as db
from Model import student_info,admin

from Dependencies import Validation
import maskpass

print('--------------- Library Management System ---------------'.center(120))
print()
while True:
    print('1. Create New Account')
    print('2. Login')
    print('3. Exit')
    print()
    choice = input('Enter Your Choice : ')

#------------------------------ New Student Registration ------------------------------

    if choice == '1':
        print('\n---------- < Create Student Account > ----------\n')
        print()
        #Name validation
        while True:
            Name=input('Enter Your Name : ')
            if Validation.NameValidation(Name):
                break
            else:
                print('\n---------- Invalid Name ---------- \n')
                
        #Address Validation
        while True:
            Address=input('Enter Your Address : ')
            if Validation.AddressValidation(Address):
                break
            else:
                print('\n---------- Invalid Address ----------\n')

        #Contact validation
        while True:
            Contact=input('Enter Your Contact : ')
            if Validation.ContactValidation(Contact):
                break
            else:
                print('\n---------- Invalid Contact ----------\n')

        #Email validation
        while True:
            Email=input('Enter Your Email : ')
            if Validation.EmailValidation(Email):
                break
            else:
                print('\n---------- Invalid Email ----------\n')

        #Password Validation
        while True:
            Password=maskpass.askpass('Enter Your Password : ',mask='*')
            if Validation.PasswordValidation(Password)==True:
                break
            else:
                print('\n---------- Invalid Password ----------\n')
        
    
        x = (Name,Address,Contact,Email,Password)
        db.Register(x)
        print()
        print('---------- < Account Created Successfully > ----------')
        print()

#------------------------------ Login Part ------------------------------

    elif choice == '2':
        print('\n---------- < Login Section > ----------\n')
        print()
        while True:
            print('1. Admin Login')
            print('2. Student Login')
            print('3. Exit')
            print()
            choice = input('Enter Your Login Choice : ')

            #------------------------------ Admin Login ------------------------------

            if choice == '1':
                print('\n---------- < Admin Login Section > ----------\n')
                print()
                #Email validation
                while True:
                    Email=input('Enter Your Email : ')
                    if Validation.EmailValidation(Email):
                        break
                    else:
                        print('\n---------- Invalid Email ----------\n')

                #Password Validation
                while True:
                    Password=maskpass.askpass('Enter Your Password : ',mask='*')
                    if Validation.PasswordValidation(Password)==True:
                        break
                    else:
                        print('\n---------- Invalid Password ----------\n')
        
                
                data = db.Admin_Login(Email,Password)
                if data == True:
                    print('\n---------- < Admin Login Successfully > ----------\n')
                    print()
                    while True:
                        print('\n---------- < Admin Choices > ----------\n')
                        print()
                      
                        print('1. Add New Book')
                        print('2. Display Student Report')
                        print('3. Modify Book Information')
                        print('4. Issue Book')
                        print('5. Delete Book')
                        print('6. Exit')
                        print()
                        choice = input('Enter Your Choice : ')
                        # Add New Book -
                        if choice == '1':
                            db.add_book()
                        elif choice == '2':
                            db.student_report()
                        elif choice == '3':
                            db.modify_book()
                        elif choice == '4':
                            db.issue_book()
                        elif choice == '5':
                            db.delete_book()
                        elif choice == '6':
                            print('\n---------- < Back in Login Page > ----------\n')
                            break
                        else:
                            print('\n---------- < Invalid Choice > ----------\n')
                #else:
                    #print('---------- < Admin Email or Password Wrong > ----------')


            #------------------------------ Student Login ------------------------------
            
            elif choice == '2':
                print('\n---------- < Student Login Section > ----------\n')
                print()
                
                #Email validation
                while True:
                    Email=input('Enter Your Email : ')
                    if Validation.EmailValidation(Email):
                        break
                    else:
                        print('\n---------- Invalid Email ----------\n')

                #Password Validation
                while True:
                    Password=maskpass.askpass('Enter Your Password : ',mask='*')
                    if Validation.PasswordValidation(Password)==True:
                        break
                    else:
                        print('\n---------- Invalid Password ----------\n')
        
                
                data = db.student_login(Email,Password)
                if data == True:
                    print('\n---------- < Student Login Successfully > ----------\n')
                    while True:
                        print('\n---------- < Student Choices > ----------\n')
                        print()
                        print('1. Search Book')
                        print('2. Report Menu')
                        print('3. Submit Book')
                        print('4. Back in Login Page')
                        print()
                        choice = input('Enter Your Choice : ')
                        # Search Book -
                        if choice == '1':
                            db.search_menu()
                        elif choice == '2':
                            db.report_menu()
                        elif choice == '3':
                            db.submit_book()
                        elif choice == '4':
                            print('\n---------- < Back in Login Page > ----------\n')
                            break
                        else:
                            print('\n---------- < Invalid Choice > ----------\n')
                else:
                    print('\n---------- < Invalid Student Details > ----------\n')

            elif choice == '3':
                print('\n--------------- < Back To Home Page > ---------------\n')
                print()
                break
            else:
                print('\n---------- < Invalid Choice > ----------\n')

    elif choice == '3':
        print('\n------------- < Thank You > ---------------\n')
        break
    else:
        print('\n---------- < Invalid Choice > ----------\n')



            






                
                    













