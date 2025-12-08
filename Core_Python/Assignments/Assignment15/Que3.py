class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        print("object is created")

    def ShowShirt(self):
        data = "\n sid :" +str(self.sid)
        data += "\n sname :"+str(self.sname)
        data += "\n type :"+str(self.type)
        data += "\n price :"+str(self.price)
        data += "\n size :"+str(self.size)
        return data
    
    def __del__(self):
        print("object get deleted")

s1=Shirt(101,"one8","formal",2300,"s",)
print(s1.ShowShirt())

    