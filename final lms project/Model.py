class student_info:
    def __init__(self,Name,Address,Contact,Email,Password):
        self.Name = Name
        self.Address = Address
        self.Contact = Contact
        self.Email = Email
        self.Password = Password
    
    def __repr__(self):
        return f'student_info[{self.Name} {self.Address} {self.Contact} {self.Email} {self.Password}]'
    
class admin:
    def __init__(self,Email,Password):
        self.Email = Email
        self.Password = Password

    def __repr__(self):
        return f'admin[{self.Email} {self.Password}]'
