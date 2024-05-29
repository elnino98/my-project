class Student_profile:
    def __init__(self,id,name,email,password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


    # to get information of student
    def get_info(self):
        return self.id , self.name , self.email

    # to get password
    def get_password(self):
        return self.password

    # to change password
    def change_pass(self , new_pass):
        self.password = new_pass




class Student:
    def __init__(self,id, name, Major,collage):
        self.id = id
        self.name = name
        self.Major = Major
        self.course = []
        self.collage = collage

    # to add course
    def add_course(self,courses):
        self.course.append(courses)
        #print(courses)

    # to veiw added course
    def veiw_course(self):
        for x in self.course:
            print(x)
    # to remove course
    def remove_course(self,course):
        self.course.remove(course)

    def veiw_student(self):
        print(self.name)



class Course:
    def __init__(self, id_course, name_course, professor_name):
        self.id_course = id_course
        self.name_course = name_course
        self.professor_name = professor_name
        self.students = []


    def add_student(self,students):
        self.students.append(students)
        #print(students)

    def veiws_students(self):
        for x in self.students:
            print(x)

    def remove_student(self,students):
        for s in self.students:
            self.students.remove(students)

    # to get data course
    def get_course_info(self):
        return self.id_course , self.name_course,self.professor_name


class Professor:
    def __init__(self,id_prof, prof_name, department):
        self.id_prof = id_prof
        self.prof_name = prof_name
        self.department = department
        self.course_teach = []

        # to add course teach
    def add_course_teach(self, courses):
        self.course_teach.append(courses)
        print(courses)

    # to remove course teach
    def remove_course_teach(self):
        for x in self.course_teach:
            print(x)

    def get_prof_info(self):
        return self.id_prof , self.prof_name , self.department



if __name__ == "__main__":


    std = Student_profile(1,'ahmad','ahmad@gmail.com','12345')
    print(std.get_info())
    print(std.get_password())
    #std.change_pass('123456')
    #print(std.get_password())



    # create object by class student
    c1 = Student(1,'ahmad', 'cs' , 'it')
    c2 = Student(2, 'omar', 'cis', 'it')
    c3 = Student(3, 'ammar', 'pi', 'it')
    c4 = Student(4, 'ali', 'mis' , 'it')

# print list [name , id , Major , college]
    list = [c1,c2,c3,c4]
    for x in list:
        print(x.id , x.name , x.Major,x.collage)

    c1.add_course('c++')
    c1.add_course('html')
    c1.add_course('C#')

    c2.add_course('jquery')
    c2.add_course('JS')
    # to remove course
    # c1.remove_course('C#')

    # to print course after added
    c1.veiw_course()
    c2.veiw_course()
    c3.veiw_course()

    # to view student
    c1.veiw_student()

    # create object from class Course
    b = Course(9101,'java','Dr.ahmad')
    b1 = Course(9102,'python','Dr.omar')

    print(b.get_course_info())
    b.add_student('ahmad')
    b.add_student('ali')

    print(b.students)
    b.veiws_students()
    # b.remove_student('ahmad')

# create object from class professor

    prof1 = Professor(2345 , 'DR.mohammad' , 'CS')
    prof2 = Professor(2346, 'DR.ahmad', 'CIS')
    prof3 = Professor(2347, 'DR.hamed', 'CS')

    list1 = [prof1 , prof2 , prof3]
    for d in list1:
        print(d.get_prof_info())

    #print(prof1.get_prof_info())

# add professor to teach course
    b3 = Course(9102, 'python', prof1.prof_name)
    print(b3.get_course_info())









