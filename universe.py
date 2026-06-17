
class Universe:

  def __init__(self,name,mass):
    self.name=name
    self.mass=mass

  def gravity(self,g):
    print(f"{self.name} has a gravitational constant {g}m/s² ")

  def creation(self):
    print(f"{self.name} was created after the Big Bang")

  
    