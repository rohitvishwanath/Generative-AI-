class Product:
    def __init__(self,pid=None,pname=None,price=None,quantity=None):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        print("the product object is created")

    def __del__(self):
        print("the product object is deleted")

    def ShowBook(self):
        data ="\n pid :"+ str(self.pid)
        data +="\n pname :"+ str(self.pname)
        data +="\n price :"+ str(self.price)
        data +="\n quantity :"+str(self.quantity)
        return data
    
# p1=Product()
# p1.ShowBook

# print()

p1=Product(101,"ikagai",12300,4)
print(p1.ShowBook())