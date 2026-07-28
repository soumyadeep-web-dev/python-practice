
class student:

  count=0
  total_gpa=0
  def __init__(self,name,gpa,):
    self.name=name
    self.gpa=gpa
    student.count +=1
    student.total_gpa=+gpa


  def get_info(self):
      return f" {self.name} {self.gpa}"
    

  @classmethod
    
  def get_count(cls):
      return f"Total number of students : {cls.count}"
  
  @classmethod

  def average(cls):
     if cls.count==0:
      return 0
     else:
        return f"{cls.total_gpa/cls.count:.2f}"
     
  @staticmethod
  def student_status(gpa):
     if gpa>5.5:
        print("Student has passed")
     else:
        print("Student has failed")
    

student1=student("Aradhya",9.4)
student2=student("Anubhabh",8.9)
student3=student("lucky",4.5)

student.student_status(4.2)

print(student.get_count())
print(student.average())