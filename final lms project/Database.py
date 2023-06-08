import mysql.connector
from mysql.connector import Error
from datetime import date
import pandas as pd
import datetime

from Dependencies import Validation


con = mysql.connector.connect(host='localhost',user='root',passwd='Mysql@10',database='lms')
print('Connection Establish Successfully')


cursor = con.cursor()

#--------------------------------- Admin Table ---------------------------------
try:
    Admin_Table = 'create table if not exists admin(Email text,Password text)'
    cursor.execute(Admin_Table)
    con.commit()
except:
    print('Table already exists')
#---------------------------------------------------------------------------------

def Admin():
    insert_query = 'insert into admin(Email,Password) values(%s,%s)'
    cursor.execute(insert_query)
    con.commit()

#--------------------------------- Admin Login ---------------------------------
def Admin_Login(Email,Password):
    select_query = 'select * from admin where Email = %s and Password = %s'
    data = (Email,Password)
    cursor.execute(select_query,data)
    s = cursor.fetchone()
   
    try:
        if s[0] == Email:
            
            if s[1] == Password:
                return True
    except:
        print('----- Invalid Email or Password -----')
    
#---------------------------------------------------------------------------------

#--------------------------------- Student_Info Table ---------------------------------

try:
    Student_Table = 'create table if not exists student_info(stud_id int auto_increment,stud_name varchar(50),stud_address varchar(50),stud_contact varchar(50),stud_Email varchar(20),stud_Password varchar(20), primary key(stud_id))'
    cursor.execute(Student_Table)
    con.commit()
except:
    print('Table already exists')
#---------------------------------------------------------------------------------

#--------------------------------- Student - Create Account ---------------------------------
def Register(x):
    register_query = 'insert into student_info(stud_name,stud_address,stud_contact,stud_Email,stud_Password) values (%s,%s,%s,%s,%s)'
    cursor.execute(register_query,x)
    con.commit()

#--------------------------------- Student Login ---------------------------------
def student_login(Email,Password):
    select_query = 'select * from student_info where stud_Email = %s and stud_Password = %s'
    data = (Email,Password)
    cursor.execute(select_query,data)
    s = cursor.fetchone()
    
    try:
        if s[4] == Email:
            if s[5] == Password:
                return True
    except:
        return 'Invalid Email-Id or Password'
#---------------------------------------------------------------------------------


#------------- Book Table ---------------

Book_Table = 'create table if not exists book(id int(10) auto_increment,title char(60) default null,author char(50) default null,pages int(4) default null,price float(6,2) default null,status char(10) default null,publisher char(60) default null,edition char(15) default null,copies int,primary key(id))'
cursor.execute(Book_Table)


#------------- Transaction Table ---------------

Transaction_Table = 'create table if not exists transaction(tid int(11) auto_increment,b_id int(11) default null,s_id int(11) default null,doi date default null,dos date default null,request_date date default null,status varchar(20),primary key(tid))'
cursor.execute(Transaction_Table)

con.commit()


# Main Program -

#--------------------------------------------------

def clear():
    for _ in range(1):
        print

#--------------------------------------------------

# Admin Login -
#--------------------------------------------------

# -------------------- Add New Book-----------------

def add_book():
    #Add Book Name
    while True:
        title=input('Enter Book Title : ')
        if Validation.TitleValidation(title):
            break
        else:
            print('\n---------- Invalid Book Name ---------- \n')

    #Author Name
    while True:
        author=input('Enter Book Author : ')
        if Validation.AuthorValidation(author):
            break
        else:
            print('\n---------- Invalid Author Name ---------- \n')

    #Publisher Name
    while True:
        publisher=input('Enter Book Publisher : ')
        if Validation.PublisherValidation(publisher):
            break
        else:
            print('\n---------- Invalid Publisher Name ---------- \n')

    #Status 
    while True:
        status=input('Enter Book Status : ')
        if Validation.StatusValidation(status):
            break
        else:
            print('\n---------- Invalid Status ---------- \n')
        
    pages = int(input('Enter Book pages : '))
    price = float(input('Enter Book price : '))
    edition = input('Enter Book edition : ')
    copies = int(input('Enter No Of Copies : '))


    '''
    title = input('Enter Book title : ')
    author = input('Enter Book author : ')
    publisher = input('Enter publisher : ')
    pages = int(input('Enter Book pages : '))
    price = float(input('Enter Book price : '))
    status = input('Enter status : ')
    edition = input('Enter Book edition : ')
    copies = int(input('Enter No Of Copies : '))
    '''
    # Insert Book Data into Book Table
    sql = f'insert into book(title,author,pages,price,status,publisher,edition,copies) values("{title}","{author}",{pages},{price},"{status}","{publisher}","{edition}","{copies}")'
    cursor.execute(sql)
    con.commit()
    print()
    print('---------- Book added successfully -----------')
    wait = input('\n\n Press any key to continue....')

#=============================================================================================================================

# -------------- Display All Books -------------

def report_book_list():
    print('\n REPORT - SHOW ALL BOOKS ')
    print('-'*120)
    sql ='select * from book'
    cursor.execute(sql)
    records = cursor.fetchall()
    rec=pd.DataFrame(records,columns=['ID','Title','Author','Pages','Price','Status','Publisher','Edition','Copies'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    if rec.empty == True:
        print('\n No Books Found ')
    else:
        print(rec)
    wait = input('\n\nPress any key to continue.....')


# -------------- Student Details (Issue and Submit Books Status) ----------------

def student_book_details():
    clear()
    print('-'*80) 
    sql ='select * from transaction'
    cursor.execute(sql)
    records = cursor.fetchall()
    rec=pd.DataFrame(records,columns=['T_ID' , 'B_ID' , 'S_ID' , 'Doi' , 'Dos' , 'Request_Date' , 'Status'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    if rec.empty == True:
        print('\n No Transactions Found ')
    else:
        print(rec)
    wait = input('\n Press any key to continue.....')


#----------- change Book Status ------------

def change_status(book_id, student_id, status):
    #sql = 'update book set status ="'+status+'" where id ='+book_id +';'
    sql1 = 'update transaction set status ="'+status+'" where b_id='+book_id +' and s_id='+student_id+';'
    #cursor.execute(sql)
    cursor.execute(sql1)
    print('\n\nBook status changed successfully')
    con.commit()
    wait = input('\n\n\n Press any key to continue....')


def student_report():
    while True:
        clear()
        print()
        print(' R E P O R T    M E N U ')
        print()
        print('\n1. Display All Books')
        print('\n2. Issue and Submit Book Details')
        print('\n3. Change Book Status')
        print('\n4. Exit to main Menu')
        print('\n')       
        choice = input('Enter Your Choice...: ')
        if choice == '1':
            report_book_list()
        if choice == '2':
            student_book_details()
        if choice == '3':
            book_id = input('Enter Book ID : ')
            student_id = input('Enter Student ID : ')
            status = input('Enter Book Status : ')
            change_status(book_id,student_id,status)
        if choice == '4':
            break

#=============================================================================================================================

# ------------------ Update Book Info ---------------

def modify_book_info(field):
   
    print('Modify BOOK Details Screen ')
    print('-'*60)
    book_id = input('Enter Book ID : ')
    value = input('Enter New Value : ')
    if field == 'pages' or field == 'price':
        sql = f'update book set {field} = "{value}" where id = {book_id}'
    else:
        sql = f'update book set {field} = "{value}" where id = {book_id}'
    cursor.execute(sql)
    con.commit()
    print()
    print('---------- Book Details Modified Successfully ----------')
    wait = input('\n\n\n Press any key to continue....')
    clear()


def modify_book():
    while True:
        print('\n1. Book Title')
        print('\n2. Book Author')
        print('\n3. Book Publisher')
        print('\n4. Book Pages')
        print('\n5. Book Price')
        print('\n6. Book Edition')
        print('\n7. Book Copies')
        print('\n8. Exit to main Menu')
        print('\n\n')
        Choice = input('Enter Your Choice : ')
        field = ''
        if Choice == '1':
            field = 'title'
        if Choice == '2':
            field = 'author'
        if Choice == '3':
            field = 'publisher'
        if Choice == '4':
            field = 'pages'
        if Choice == '5':
            field = 'price'
        if Choice == '6':
            field = 'edition'
        if Choice == '7':
            field = 'copies'
        if Choice == '8':
            break
        modify_book_info(field)

#=============================================================================================================================

# -------------- Delete Book -----------------

def delete_book():
    clear()
    print(' DELETE BOOK SCREEN ')
    print('-'*100)
    ac=input('Enter Book ID : ')
    sql ='delete from book where id =%s'
    data=(ac,)
    cursor.execute(sql,data)
    con.commit()
    print('\n Book Deleted Successfully')
    wait = input('\n Press any key to continue....')

#====================================================================================================================

# ------------- Issue Book ---------------

def stud_issue_status(student_id):
    sql ='select * from transaction where s_id ='+student_id +' and dos is NULL;'
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def book_status(book_id):
    sql = 'select * from book where id ='+book_id + ';'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[5]

def book_issue_status(book_id,student_id):
    sql = 'select * from transaction where b_id ='+book_id +' and s_id ='+student_id +' and dos is NULL;'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def issue_book():
    clear()
    print('\n BOOK ISSUE SCREEN ')
    print('-'*100)

    book_id = input('Enter Book ID : ')
    student_id = input('Enter Student ID : ')

    result = book_status(book_id)
    result1 = stud_issue_status(student_id)

    today = date.today()
    if len(result1) == 0:
        if result == 'available':
            sql = 'insert into transaction(b_id, s_id, doi) values('+book_id+','+student_id+',"'+str(today)+'");'
            sql_book = 'update book set status="issue" where id ='+book_id + ';'
            cursor.execute(sql)
            cursor.execute(sql_book)
            print('\n\n\n Book issued successfully')
        else:
            print('\n\nBook is not available for ISSUE... Current status :',result1)
    else:
        if len(result1) < 1:
            sql = 'insert into transaction(b_id, s_id, doi) values(' +book_id+','+student_id+',"'+str(today)+'");'
            sql_book = 'update book set status="issue" where id ='+book_id + ';'
            cursor.execute(sql)
            cursor.execute(sql_book)
            print('\n\n\n Book issued successfully')
        else:
            print('\n\nStudent already have book from the Library')
    con.commit()
    wait = input('\n\n\n Press any key to continue....')

#====================================================================================================================


# Student Login - 
#--------------------------------------------------

# ------------ Search Book --------------

def search_book(field):
    clear()
    print('\n BOOK SEARCH SCREEN ')
    print('-'*100)
    msg ='Enter '+ field +' Value :'
    title = input(msg)
    sql ='select * from book where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for :',field,' :' ,title)
    print('-'*100)
    rec=pd.DataFrame(records,columns=['ID','Title','Author','Pages','Price','Status','Publisher','Edition','Copies'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    if rec.empty == True:
        print('\n No Books Found ')
    else:
        print(rec)

    #for record in records:
      #print(record)  
    wait = input('\n Press any key to continue....')

def search_menu():
    while True:
        clear()
        print()
        print(' S E A R C H   M E N U ')
        print()
        print("\n1.  Book Title")
        print('\n2.  Book Author')
        print('\n3.  Publisher')
        print('\n4.  Exit to main Menu')
        print('\n\n')
        choice = input('Enter Your Choice...: ')
        field =''
        if choice == '1':
            field= 'title'
        if choice == '2':
            field = 'author'
        if choice == '3':
            field = 'publisher'
        if choice == '4':
            break
        search_book(field)

#===========================================================================================================

# Report Menu -

# ------------- Display Available Books ------------------

def report_available_books():
    clear()
    print('\n REPORT - BOOK TITLES - Available')
    print('-'*120)
    sql = 'select * from book where status = "available";'
    cursor.execute(sql)
    records = cursor.fetchall()
    rec=pd.DataFrame(records,columns=['ID','Title','Author','Pages','Price','Status','Publisher','Edition','Copies'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    if rec.empty == True:
        print('\n No Books Found ')
    else:
        print(rec)
    #for record in records:
       #print(record)
    wait = input('\n Press any key to continue.....')


# --------------- Request For Book ----------------

def add_student_request(b_id,s_id):
    clear()
    request_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = con.cursor()
    q = 'insert into transaction(b_id,s_id,request_date) VALUES (%s, %s, %s)'
    val = (b_id,s_id,request_date)
    cursor.execute(q,val)
    con.commit()
    print('\n Request Submitted Successfully.Please Collect Book After 2 Days... ')
    wait = input('\n Press any key to continue....')


#----------- Display Book Request Status ----------

def display_request_status():
    sql = 'select b_id,s_id,request_date,status from transaction'
    cursor.execute(sql)
    result = cursor.fetchall()
    print('\n Request Book Status ')
    print('-'*50)
    
    rec = pd.DataFrame(result,columns=['B_ID' , 'S_ID' , 'Request_Date' , 'Status'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    if rec.empty == True:
        print('No Request Book Status Found')
    else:
        print(rec)
    wait = input('\n Press any key to continue....')



def report_menu():
    while True:
        clear()
        print()
        print(' R E P O R T    M E N U ')
        print()
        print("\n1.  Available Books")
        print('\n2.  Request For Book')
        print('\n3.  Display Book Request Status')
        print('\n4.  Exit to main Menu')
        print('\n')    

        choice = input('Enter Your Choice...: ')
        if choice == '1':
            report_available_books()
        if choice == '2':
            b_id = input('Enter Book Id : ')
            s_id = input('Enter Student Id : ')
            add_student_request(b_id,s_id)
        if choice == '3':
            display_request_status()
        if choice == '4':
            break

    
#=====================================================================================

# ------------- Submit Book ------------

def submit_book():
    
    clear()
    print('\n BOOK SUBMIT SCREEN ')
    print('-'*100)

    book_id = input('Enter Book ID : ')
    student_id = input('Enter Student ID : ')
    today = date.today()
    result = book_issue_status(book_id,student_id)
    if result==None:
       print('Book was not issued...Check Book Id and Student ID again...')
    else:
       sql='update book set status ="available" where id ='+book_id +';'
       
       sql1 ='update transaction set dos ="'+str(today)+'" where b_id='+book_id +' and s_id='+student_id+' and dos is NULL;' 
       
       cursor.execute(sql)
       cursor.execute(sql1)
       print('\n\nBook submitted successfully')
    con.commit()
    wait = input('\n\n\n Press any key to continue....')

#====================================================================================================================
