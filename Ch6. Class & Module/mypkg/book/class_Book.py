class Book:
    def __init__(self, 제목, 단가, 재고):
        self.title = 제목
        self.price = 단가
        self.stock = 재고
        
    def change_price(self, 가격):
        self.price = 가격
        
    def change_stock(self, 수량):
        self.stock += 수량
        
    def show_stock(self):
        print(self.stock)