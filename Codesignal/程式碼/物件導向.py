#建立一個 Student 類別
class Student:
    #constructor 建構子
    #self 代表物件本身
    #self.name, self.grade 代表物件的屬性
    count=0
    def __init__(self,name,grade):
        self.name=name
        #指定屬性grade為私有的
        self.__grade=grade
        Student.count+=1
    #物件的方法名稱displayStudent
    def displayStudent(self):
        print('name='+self.name)
        print('grade='+str(self.__grade))
    #物件的方法名稱whoami    
    def whoami(self):
        return self.name
    def myGrade(self):
        return self.__grade
    def setGrade(self,grade):
        self.__grade=grade
    
s1=Student('Tom',80)
s1.displayStudent()
myname=s1.whoami()
mygrade=s1.myGrade()
print(myname)
print("所有學生人數 = ", Student.count, s1.count)

class Vehicle:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
        
    def getName(self):
        return self.__name
    

# Car 類別繼承 Vehicle 類別
class Car(Vehicle):
    # 屬性 model 是 Car 類別專有的
    def __init__(self, name, color, model):
        # 呼叫父類別的建構子
        super().__init__(name, color)
        self.__model = model
    
    def displayCar(self):
        print("名稱=", self.getName())
        print("車型=", self.__model)
        print("顏色=", self.getColor())
  
c1 = Car("Ford", "Black", "GT350")
c1.displayCar()
c1.getName()

c2 = Car("Benz", "Blue", "Z100")
c2.displayCar()

class Circle:
    def __init__(self,radius):
        self.__radius=radius
    def setRadius(self,radius):
        self.__radius=radius
    def getRadius(self):
        return self.__radius
    def area(self):
        return 3.14*self.__radius**2
    def __add__(self,circle2):
        return Circle(self.__radius+circle2.__radius)
    def __gt__(self,circle2):
        return self.__radius > circle2.__radius
    def __it__(self,circle2):
        return self.__radius < circle2.__radius
    def __str__(self):
        return '圓半徑='+str(self.__radius)
    
c1 = Circle(10)
c2 = Circle(20)
c3 = c1 + c2
print(c3.getRadius())
print(c1 > c2)
print(c1 < c2)
print(str(c1))











