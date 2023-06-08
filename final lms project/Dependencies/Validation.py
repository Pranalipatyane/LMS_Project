import re

#Name validation
def NameValidation(name):
    ptr='^[a-zA-Z\ ]+$'
    if re.match(ptr,name):
        return True
    else:
        return False
    
#Address validation
def AddressValidation(address):
    ptr='^[a-zA-Z0-9\.\s\-\,]'
    if re.match(ptr,address):
        return True
    else:
        return False    
  
#Contact validation
def ContactValidation(contact):
    ptr='^[6-9]+[0-9]{9}'
    if re .match(ptr,contact):
        return True
    else:
        return False
    
#Email validation
def EmailValidation(email):
    ptr='^[a-z0-9\.\_]+@[a-z]+\.[com|org|in]+$'
    if re.match(ptr,email):
        return True
    else:
        return False

#Password Validation
def PasswordValidation(password):
    
    if len(password) >= 8:
        return True
    else:
        return 'Password Length is less than 8'
    

#--------------------------------------------------------

#Add Book - Validation

#Title validation
def TitleValidation(title):
    ptr='^[a-zA-Z\ ]+$'
    if re.match(ptr,title):
        return True
    else:
        return False
    
#Author validation
def AuthorValidation(author):
    ptr='^[a-zA-Z\ ]+$'
    if re.match(ptr,author):
        return True
    else:
        return False

#Publisher validation
def PublisherValidation(publisher):
    ptr='^[a-zA-Z\ ]+$'
    if re.match(ptr,publisher):
        return True
    else:
        return False
    
#Status validation
def StatusValidation(status):
    ptr='^[a-zA-Z\ ]+$'
    if re.match(ptr,status):
        return True
    else:
        return False
    