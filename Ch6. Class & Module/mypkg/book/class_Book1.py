from class_Book import Book

class Book1(Book): #'Book' class의 child class
    def __init__(self,book): #parent의 __init__ method를 override(대체)
        self.title = book[0]
        self.price = book[1]
        self.stock = book[2]
        if len(book) >3:
            self.publisher = book[3]
    
    def showinfo(self):
        print(f'{self.title}: {self.price:6.1f}원 {self.stock:3d}권')