class Student:
    def getData(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def  displayStudent(self):
         print("Roll Number:",self.rollno)
         print("Name",self.name)
         print("Course",self.course)

    #inheritance
class Test(Student):
    
    def getMarks(self,mark):
            self.mark=mark
    def displayMark(self):
             print("Total Marks:",self.mark)


             #multilvelInheritance
class Result (Test):
    def calculateGrade(self):
        if self.mark>480:self.grade="Distiction"
        elif self.mark>360:self.grade="First class"
        elif self.mark>240:self.grade="Second class"
        else:self.grade="Failed"
        print("RESULT:",self.grade)

#Main program
r=int(input("Enter Roll Number:"))
n=input("Enter Name:")
c=input("Enter Course:")
m=int(input("Enter Mark:"))

#create object
print("\nRESULT")
stud1=Result()
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.displayStudent()
stud1.displayMark()
stud1.calculateGrade()

        
   
             
