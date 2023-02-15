class libraryManagementSystem:
    def Login():
        pass
    def Register():
        pass
    def Logout():
        pass
    def __init__(self,UserType,Username, Password) -> None:
        self.UserType = UserType
        self.Username = Username
        self.Password = Password

Libary1 = libraryManagementSystem( "Admin", "Mrs Blessing", "Admin101")
print(Libary1.Username)
class User:
    def __init__(self, Name, Id) -> None:
        self.Name = Name
        self.Id = Id

class Liberian:
    def __init__(self,Name, Id, Password, SearchString) -> None:
        self.Name = Name
        self.Id = Id
        self.Password = Password
        self.SearchString = SearchString

class Book:
    def __init__(self,Title, Author, ISBN, Publication) -> None:
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
        self.Publication = Publication
    
class Account:
    def __init__(self,no_borrowed_books,no_reserved_books,no_lost_booksfine_amount) -> None:
        self.borrowedbooks = no_borrowed_books
        self.reservedbooks = no_reserved_books
        self.lostbookfine = no_lost_booksfine_amount
    

class libraryDatabase:
    def __init__(self,List_of_books) -> None:
        self.listofbooks = List_of_books
        
class Staff:
    def __init__(self, department) -> None:
        self.departmemt = department

class Student:
    def __init__(self, Class) -> None:
        self.Class = Class

    