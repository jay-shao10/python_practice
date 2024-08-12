# 物件(object)是類別(class)的實例(instance)

# 車=>類別class
# 每一台生產出來的車子=>物件 object
class Car:
    # 類別變數
    wheels=4

    # 屬性 初始化
    def __init__(self,make,model,year,color):
        
        self.make=make
        self.model=model
        self.year=year
        self.color=color

    # 功能性，函式
    def drive(self):
        print(self.model+"正在行駛")
        return self
    
    def stop(self):
        print(self.model+"已停止")
        return self

car1=Car("Toyota","Altis",2021,"blue")
car2=Car("Ford","Kuga",2020,"black")

# print(car1) 
#輸出<__main__.Car object at 0x0000020320161A50>

# 測試上面代碼
# print(car1.make)
# car1.drive()
# car2.stop()

# 以下叫做方法鏈
# car1.stop().drive()


# python中的繼承，父類別跟子類別
class Animal:
    alive=True

    def eat(self):
        print("這個動物正在吃東西")

    def sleep(self):
        print("這個動物正在睡覺")

class Rabbit(Animal):

    def eat(self):# python中的方法重寫(method overriding)
        print("兔子正在吃蘿蔔")

    def jump(self):
        print("這隻兔子正在跳")

# 測試上面代碼
# animal=Animal()
# rabbit=Rabbit()
# rabbit.jump()
# rabbit.eat()




# 物件導向的super方法
class Rectengle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        print("初始化完成")

class cube(Rectengle):
    def __init__(self, length, width,height):

        # 重複利用程式碼的效果，讓程式更淺顯易懂
        super().__init__(length, width)
        self.height=height
        print(f"立方體的長寬高是{length},{width},{height}")

c=cube(10,20,30)