from TaskOne import TxtWriter, StudentGroup, StudentMark


# work with class TxtWriter
def read_student_group_from_file():
    print('Enter name of group:')
    name = input()
    txt = TxtWriter()
    return txt.get_studentGroup_from_txt(name)


# work with class StudentGroup
def get_information_selected_student(info):
    print("Enter name of student:")
    name = input()
    try:
        print(info.dictMark[name])
    except KeyError as e:
        print(e)
def get_total_mark(info):
    print("Enter name of student:")
    name = input()
    list_of_marks=info.dictMark[name]
    total_mark=list_of_marks.getTotalMark()
    print(name,'total',total_mark)

information = ' '
print('Welcome!')
while True:
    print(
          '\n'+'Choose section and enter number of it:' + '\n' +
          '1. Read marks a group from file' + '\n' +
          '2. View marks' + '\n' +
          '3. View marks of selected student'+'\n'+
          '4. View total mark of selected student')
    num = int(input())
    if num == 1:
        information = read_student_group_from_file()
    elif num == 2:
        print(information)
    elif num == 3:
        get_information_selected_student(information)
    elif num==4:
        get_total_mark(information)
