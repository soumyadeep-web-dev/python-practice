from universe import Universe

class stellar_objects(Universe):
  def plasma(self):
    print(f"{self.name} is composed of hot plasma")


class solarSystem_objects(Universe):
  def binding(self):
    print(f"{self.name} is gravitationally connected to other celestial bodies")
  

class planets(solarSystem_objects):
  pass

class black_Holes(stellar_objects):
  pass

class stars(stellar_objects,solarSystem_objects):
  pass


planet1=planets("Jupiter", 1.898 )


print(planet1.name)
print(planet1.mass)
planet1.gravity(24.79)
planet1.binding()