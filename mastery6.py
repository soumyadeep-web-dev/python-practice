from abc import ABC , abstractmethod
class shape(ABC):
   
   

   
   
   @abstractmethod
   def area(self):
      pass
     
  
class circle(shape):

  def __init__(self,radius):
    self.radius=radius
    

  
  def area(self):
   return 3.14*self.radius**2

class square(shape):
  def __init__(self,width):
    self.width=width
   
    
  def area(self):
   return self.width*self.width



class triangle(shape):
  def __init__(self,base,height):
    
    self.base=base
    self.height=height
    
    
  def area(self):
   return 1/2*(self.base)*(self.height)



shapes=[circle(4),square(6),triangle(5,2)]


for shape in shapes:
  print(shape.area())


