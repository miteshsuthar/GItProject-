class Student:
	cname="Cpt"
	def __init__(self,rollno):
		self.rollno=rollno
s=Student(1)
s1=Student(2)
s.name = "abx"
print(s.__dict__)
print(s1.__dict__)
print(Student.__dict__)
