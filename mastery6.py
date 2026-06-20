from abc import ABC , abstractmethod
class shape(ABC):
   
   def __init__(self,color,is_filled):
     self.color=color
     self.is_filled=is_filled

   def property(self):
     print(f"Color is {self.color} and {"filled" if self.is_filled else "Not filled"}")
   
   @abstractmethod
   def area(self):
      pass
     
  
class circle(shape):

  def __init__(self,color, is_filled,radius):
    self.radius=radius
    super().__init__(color,is_filled)

  def property(self):
    print("Its round and its area is measued using its area and pi")
    super().property()
  
  def area(self,radius):
   return 3.14*radius**2

class square(shape):
  def __init__(self,color,is_filled,width):
    self.width=width
    super().__init__(color,is_filled)
    
  def area(self,width):
   return width*width



class triangle(shape):
  def __init__(self,color,is_filled,base,height):
    
    self.base=base
    self.height=height
    super().__init__(color,is_filled)
    
  def area(self,base,height):
   return 1/2*(base)*(height)



circle1=circle("red",True,4)
square1=square("green",False,6)
triangle1=triangle("blue",False,5,2)


