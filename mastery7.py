class shapes:
  def __init__(self,color,is_filled):
    self.color=color
    self.is_filled=is_filled

  def greeting(self):
      print(f"It is {self.color} and {'filled'if self.is_filled else 'not filled'} ")

class circle(shapes):
  def __init__(self,radius,color,is_filled):
    super(). __init__(color,is_filled)
    self.radius=radius

class square(shapes):
  def __init__(self,color,is_filled,side):
    super(). __init__(color,is_filled)
    self.side=side
  
  def greeting(self):
    print(f"Hello I am a Square")
    super(). greeting()


class triangle(shapes):
  def __init__(self,color,is_filled,base,height):
    super(). __init__(color,is_filled)
    self.height=height
    self.base=base

circle1=circle(7,"blue","False")
square1=square("red","True",8)
circle1.greeting()
square1.greeting()