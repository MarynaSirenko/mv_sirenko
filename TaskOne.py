import os

class StudentGroup():
    def __init__(self, nameGroup, nameSubject):
        self.nameGroup = nameGroup
        self.nameSubject = nameSubject
        self.dictMark = {}

    def add_student_marks(self, student_fullname, list_of_marks):
        self.dictMark[student_fullname] = list_of_marks

    def __str__(self):
        result='\t' + self.nameGroup + '\n' + self.nameSubject + '\n'
        for key,item in self.dictMark.items():
            result+=key+':'
            for x in item.marks:
                result+=' '+ str(x)
            result+='\n'
        return result


    def get_mark_selected_student(self, name):
        self.name = name
        if name in self.dictMark:
            return self.dictMark[name]
        else:
            raise KeyError("Student isn't from this group")


# for work with mark
class StudentMark():
    def __init__(self, marks):
        self.marks = marks

    def __str__(self):
        result=''
        for x in self.marks:
            result+=str(x)+' '
        return result


    def getTotalMark(self):
        a = 0
        for i in self.marks:
            a += i
        return a / len(self.marks)


class TxtWriter:
    def get_studentGroup_from_txt(self, student_group_name="2.КИТ.8"):
        with open(student_group_name + '.txt')as file:
            nameSubject = file.readline()
            nameGroup = student_group_name
            student_group_dict = StudentGroup(nameGroup, nameSubject)
            _ = file.readline()
            for line in file:
                line = line.split()
                name=line[0]
                list_of_marks=StudentMark([ int (i) for i in line[1:]])
                student_group_dict.add_student_marks(name, list_of_marks)
            return student_group_dict


