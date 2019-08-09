class Studengt:
    def __init__(self ,name,score,age):
        self.name =name
        self.score =score
        self.age = age
    def __str__(self):
        return "竹林居士%s,星级%d,性别%s"%(self.name,self.score,self.age)
    def __repr__(self):
            return "竹林居士%s,星级%d,性别%s"%(self.name,self.score,self.age)

student = Studengt("swn",88,25)
print(student)
student1 = student.__repr__()
print(student1)
student02 = "sdasdsa"
student03 = eval(student02.__repr__())
print(student03)
student04 = eval(student1.__repr__())
print(student04)


# print(student.__str__())
# student2 = eval(student.__repr__())
# print(student2)