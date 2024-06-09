# flex-ops-training

* create class userAccount

```python
class UserAccount:
    def __init__(self):
        self.users = []

    def sign_up(self, students_profile):

        # Check if any of the fields are empty
        if not name.strip() or not email.strip() or not password.strip() or not repeat_password.strip():
            print("Please fill in all the fields.")
            return False

        # Check if the email already exists
        for user in self.users:
            if user['email'] == email:
                print("Email already exists. Please use a different email.")
                return False

        # Check if passwords match
        if password != repeat_password:
            print("Passwords do not match.")
            return False

        # If all checks pass, add the user to the list
        self.users.append({'id': id, 'name': name, 'email': email, 'password': password})
        print("Account created successfully.")
        return True

    def login(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                print("Login successful.")
                return True
        print("Invalid email or password.")
        return False
```

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
* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **get_info** method used to get information by student
* The **get_password** method to get  a password of student
* The **change_pass** method to change a password students


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
* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **add_course** method used to add course  student
* The **veiw_course** method to view added course   
* The **remove_course** method to remove a course 
* Tho **view_students** method to view student take a course 


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

* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **add_student** method used to add students
* The **veiws_student** method to print name student if student take a course     
* The **remove_course** method to remove a student take a course  
* Tho **get_course_info** method to print information course 


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

* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **add_course_teach** method used to add course 
* The **veiw_course_teach** method to view a course teach   
* The **remove_course_teach** method to remove a course teach 
* Tho **get_prof_info** method to get information teacher



* to check programme is run code and show result:
```python
      if __name__ == "__main__":
```



* after   if __name__ == "__main__":

```python
    account_manager = UserAccount()
    std = Student_profile(1,'ahmad','ahmad2','12345','12345')

    #account_manager.sign_up(1,'ahmad','ahmad2','12345','12345')




    id = input("Enter your ID: ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    repeat_password = input("Repeat your password: ")

    #account_manager.sign_up(id, name, email, password, repeat_password)

    student_profile = Student_profile(id, name, email, password, repeat_password)
    account_manager.sign_up(student_profile)

    email = input("Enter your email: ")
    password = input("Enter your password: ")


    user_logged_in = account_manager.login(email, password)

    if user_logged_in:
        while True:
            print('1. get informaition')
            print('2. get password')
            print('3. Exit...')

            num = int(input('Enter your choice (1: Get Info, 2: Get Password, 3: Exit): '))

            if num == 1:
                print(student_profile.get_info())
            elif num == 2:
                print(student_profile.get_password())
            elif num == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
```
    


