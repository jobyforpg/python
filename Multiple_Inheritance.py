class Student:
    def getData(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def  displayStudent(self):
         print("Roll Number:",self.rollno)
         print("Name",self.name)
         print("Course",self.course)

class Test(Student):
    
    def getMarks(self,mark):
            self.mark=mark
    def displayMark(self):
             print("Total Marks:",self.mark)
             
 class Sports:
     def getSportsMarks(self,spmarks):
         self.spmarks=spmarks
         def displaySportsMarks(self):
             print("sports Marks:",self.spmarks)

#Multiple Inheritance
class Result(Test,Sports):
    def calculateGrade(self):
        m=self.marks+self.spmarks
        if m>480:self.grade="Distinction"
        elif>360:self.grade="First Class"
        elif>240:self.grade="second Class"
        else>self.grade="Failed"
        print("RESULT",self.grade)

#main program
r=int(input("Enter Roll Number:"))
n=input("Enter Name:")
c=input("Enter Course:")
m=int(input("Enter Mark:"))
s=int(input("Enter Sports Mark:"))

#create the object
stud1=Result()
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.displayStudent()
stud1.displayMark()
stud1.calculateGrade()


        
        

         

