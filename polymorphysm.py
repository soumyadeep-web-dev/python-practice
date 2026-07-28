
class Shape:
   
   def area(self):
     pass

class circle(Shape):
 def __init__(self,radius):
   self.radius=radius

 def area(self):
   return 3.14*self.radius**2
     



class square(Shape):
  def __init__(self,side):
   self.side=side

  def area(self):
   return self.side*self.side


class triangle(Shape):
  def __init__(self,base,height):
   self.base=base
   self.height=height

  def area(self):
    return 0.5*self.base*self.height
  
class pizza(circle):
  def __init__(self,toppings,radius):
    self.toppings=toppings
    super().__init(radius)



shapes=[circle(4),square(5),triangle(6,7),pizza("peparoni",6)]

for shape in shapes:
 print(shape.area()) 