class Book:
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        print("Book objcet created")

    def __del__(self):
        print("Book object destroyer")

    def showBook(self):
        data ="\n bid     : " + str(self.bid)
        data +="\n bname  :" + str(self.bname)
        data +="\n price  :"+ str(self.price)
        data +="\n author :"+ str(self.author)
        return data
        
    # ------- Driver code ---------
# b1=Book() # parameterless
# b1.showBook()

# print()

b2=Book(101,"python",450,"ABC Publication")
print(b2.showBook())    
