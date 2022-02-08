class Student:
	cname ="CPT"
	
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name 
s=Student(1,"abc")
s1=Student(2,"cse")
s.cname="csd"
print(s.rollno,s.cname)
print(s1.rollno,s1.cname)
del s1.rollno
print(s.rollno,s.name,s.cname)
print(s1.rollno,s1.cname)
del Student.cname
print(s.rollno,s.name,s.cname)
print(s1.rollno,s1.cname)
