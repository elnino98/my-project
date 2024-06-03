# flex-ops-training

* create class student_profile :

```python
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
 ```
The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
The **get_info** method used to get information by student
The **get_password** method to get  a password of student
The **change_pass** method to change a password students

* create class Student :
```python
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

      # to display a student
         def veiw_student(self):
             print(self.name)


 ```
The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
The **add_course** method used to add course  student
The **veiw_course** method to view added course   
The **remove_course** method to remove a course 
Tho **view_students** method to view student take a course 

* create class Course :

```python
    class Course:
        def __init__(self, id_course, name_course, professor_name):
            self.id_course = id_course
            self.name_course = name_course
            self.professor_name = professor_name
            self.students = []

        # to add student
        def add_student(self,students):
            self.students.append(students)
            #print(students)
       
        # to view student
        def veiws_students(self):
            for x in self.students:
                print(x)

       # to remove student 
       def remove_student(self,students):
           for s in self.students:
               self.students.remove(students)

       # to get data course
       def get_course_info(self):
           return self.id_course , self.name_course,self.professor_name

 ```

The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
The **add_student** method used to add students
The **veiws_student** method to print name student if student take a course     
The **remove_course** method to remove a student take a course  
Tho **get_course_info** method to print information course 

* create class Profissor :

```python
    class Profissor:
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
       
 ```

The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
The **add_course_teach** method used to add course 
The **veiw_course_teach** method to view a course teach   
The **remove_course_teach** method to remove a course teach 
Tho **get_prof_info** method to get information teacher



* to check programme is run code and show result:
```python
      if __name__ == "__main__":
```
* Then create object used class student_profile write :
```python

      std = Student_profile(1,'ahmad','ahmad@gmail.com','12345')
      print(std.get_info())
      print(std.get_password())
```
* Output:

      (1, 'ahmad', 'ahmad@gmail.com')
      12345

* to change a password and print new password write :
```python

      std.change_pass('123456')
      print(std.get_password())
```
*  Output :

       123456


* create object by class student write code :
```python

    c1 = Student(1,'ahmad', 'cs' , 'it')
    c2 = Student(2, 'omar', 'cis', 'it')
    c3 = Student(3, 'ammar', 'pi', 'it')
    c4 = Student(4, 'ali', 'mis' , 'it')
```
* to  print list [name , id , Major , college] write code :

```python
    list = [c1,c2,c3,c4]
    for x in list:
        print(x.id , x.name , x.Major,x.collage)
```
* Output:


    1 ahmad cs it
    2 omar cis it 
    3 ammar pi it
    4 ali mis it

* to add course to c1 & c2  write code :

```python
    c1.add_course('c++')
    c1.add_course('html')
    c1.add_course('C#')
    c2.add_course('jquery')
    c2.add_course('JS')

```
* to print course after added

```python
    c1.veiw_course()
    c2.veiw_course()
    c3.veiw_course()

```

* Output:

      c++
      html
      C#
      jquery
      JS


* to remove course after added course write :
```python
     c1.remove_course('C#')
```
  * to view student

```python
    c1.veiw_student()
```

* Output :

      ahmad


* create object from class Course write : 
```python

      b = Course(9101,'java','Dr.ahmad')
      b1 = Course(9102,'python','Dr.omar')
```
* print course information write code:

```python
    print(b.get_course_info())
```
* Output :

      (9101, 'java', 'Dr.ahmad')

* to add student in course and print student :

```python
    b.add_student('ahmad')
    b.add_student('ali')
    print(b.students)
```
* Output:

      ['ahmad', 'ali']
* another ways to print student used method :
```puthon
    b.veiws_students()
```
* Output:


    ahmad
    ali

* to remove student used **remove_student** method like :

```python
    b.remove_student('ahmad')
```

* To create object from class professor :
```python
      prof1 = Professor(2345 , 'DR.mohammad' , 'CS')
      prof2 = Professor(2346, 'DR.ahmad', 'CIS')
      prof3 = Professor(2347, 'DR.hamed', 'CS')
```
* to print professor information prof1 , prof2 , prof3 write : 
```python
      list1 = [prof1 , prof2 , prof3]
      for d in list1:
          print(d.get_prof_info())
```

* Output :

      (2345, 'DR.mohammad', 'CS')
      (2346, 'DR.ahmad', 'CIS')
      (2347, 'DR.hamed', 'CS')


* to print prof1 or prof2 or prof3 write code below : 
```python
      print(prof1.get_prof_info())
```
* Output :

      (2345, 'DR.mohammad', 'CS')

* add professor to teach course and show professor and course details :
```python

    b3 = Course(9102, 'python', prof1.prof_name)
    print(b3.get_course_info())

```
* Output:


    (9102, 'python', 'DR.mohammad')

    

# flex-ops-training
# elnino98
# flex-ops-training
# flex-ops-training
