class shape(ABC):
    @abstractmethod
    def area(self):
        print("Area method")
    def perimeter(self):
        print("Perimeter method")
        
class Circle(shape):
    def area(self):
        print("Circle area")
    def perimeter(self):
        print("Circle perimeter")
    def total(self):
        print("Total")
        
class Rectangle(shape):
    def area(self):
        print("Rectangle area")
    def perimeter(self):
        print("Rectangle perimeter")
    def total(self):
        print("Total")

c = Circle()
r = Rectangle()

c.area()
c.perimeter()

r.area()
r.perimeter()