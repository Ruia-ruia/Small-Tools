#Iterator Object - contains __next__()
class IterTeacher:
    def __init__(self, teachers_list):
        self.teachers_list = teachers_list
        self.cursor = 0

    def __next__(self):
        if self.cursor == len(self.teachers_list):
            raise StopIteration
        
        retval = self.teachers_list[self.cursor]
        self.cursor += 1

        return retval
        

#Iterable Object - contains __iter__()
class School:
    def __init__(self, name):
        self.name = name 
        self.teachers = []

    def add_teacher(self, teacher):
        if not isinstance(teacher, str):
            raise ValueError("Teacher argument not string")

        if teacher not in self.teachers: 
            self.teachers.append(teacher)
        
    def __iter__(self):
        return IterTeacher(self.teachers)
        
    def __str__(self):
        return self.name + ' is the name of the school.'

sco = School("summer heights")
sco.add_teacher("Mr. G")
sco.add_teacher("Mr. F")
sco.add_teacher("Mr. N")
sco.add_teacher("Mr. T")

print(sco)

g = iter(sco)
for i in range(4):
    print(next(g))
