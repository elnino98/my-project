# my first project

* create class userAccount

```python
class UserAccount:
    def __init__(self):
        self.users = []

    def sign_up(self, student_profile):
        name = student_profile.name
        email = student_profile.email
        password = student_profile.password
        repeat_password = student_profile.repeat_password

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
        self.users.append({'id': student_profile.id, 'name': name, 'email': email, 'password': password})
        print("Account created successfully.")
        return True

    def login(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                print("Login successful.")
                return user['id'], user['name']
        print("Invalid email or password.")
        return None, None


    def sign_up_prof(self, prof_profile):
        name = prof_profile.name
        email = prof_profile.email
        password = prof_profile.password
        repeat_password = prof_profile.repeat_password

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
        self.users.append({'id': prof_profile.id, 'name': name, 'email': email, 'password': password})
        print("Account created successfully.")
        return True


    def login_prof(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                print("Login successful.")
                return user['id'], user['name']
        print("Invalid email or password.")
        return None, None


```
* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **sign_up** method used to sign up students
* The **login** method used to login student account
* The **sign_up_prof** method used to create account professor
* The **login_prof** method used to login professor


* create class student_profile :

```python
class StudentProfile:
    def __init__(self, id, name, email, password, repeat_password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password



    def get_info(self):
        return self.id, self.name, self.email

    # to get password
    def get_password(self):
        return self.password

    # to change password
    def change_pass(self, new_pass, repeat_new_pass):
        if new_pass != repeat_new_pass:
            print("New passwords do not match.")
            return False
        self.password = new_pass
        print("Password changed successfully.")
        return True
 ```
* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **get_info** method used to get information by student
* The **get_password** method to get  a password of student
* The **change_pass** method to change a password students


* create class Student :
```python
class Student:
    def __init__(self, id, name, major, collage):
        self.id = id
        self.name = name
        self.major = major
        self.courses = []
        self.collage = collage

    # to add course
    def add_course(self, course):
        self.courses.append(course)
        print(f"Course {course.id_course} added successfully.")

    # to view added course
    def view_courses(self):
        if not self.courses:
          print("No courses added.")
        else:  
            for course in self.courses:
                print(course.get_course_info())

    # to remove course
    def remove_course(self, course_id):
        self.courses = [course for course in self.courses if course.id_course != course_id]
        print(f"Course {course_id} removed successfully.")

    def get_student_info(self):
        return self.id, self.name, self.major, self.collage

 ```
* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **add_course** method used to add course  student
* The **veiw_course** method to view added course   
* The **remove_course** method to remove a course 
* Tho **get_student_info** method to get student information 


* create class Course :

```python
class Course:
    def __init__(self, id_course, name_course, professor):
        self.id_course = id_course
        self.name_course = name_course
        self.professor_name = professor.prof_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        #print(f"Student {student.id} added to course {self.id_course}.")

    def view_students(self):
        if not self.students:
            print("No students enrolled.")
        else:
            for student in self.students:
                print(student.get_student_info())

    def get_course_info(self):
        return self.id_course, self.name_course, self.professor_name
 ```

* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **add_student** method used to add students
* The **veiws_student** method to print name student if student take a course     
* The **remove_course** method to remove a student take a course  
* Tho **get_course_info** method to print information course 

* create class professorProfile:
```python
class ProfessorProfile:
    def __init__(self, id, name, email, password, repeat_password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

    # to get information of student
    def get_info(self):
        return self.id, self.name, self.email

    # to get password
    def get_password(self):
        return self.password

    # to change password
    def change_pass(self, new_pass, repeat_new_pass):
        if new_pass != repeat_new_pass:
            print("New passwords do not match.")
            return False
        self.password = new_pass
        print("Password changed successfully.")
        return True
```
* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **get_info** method used to get information by professor
* The **get_password** method to get  a password of professor
* The **change_pass** method to change a password professor

* create class Professor :

```python
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
 ```

* The **__init__** method, also known as the constructor, is a special method in Python classes. It is automatically called when a new instance of the class is created.
* The **add_course_teach** method used to add course 
* The **veiw_course_teach** method to view a course teach   
* The **remove_course_teach** method to remove a course teach 
* Tho **get_prof_info** method to get information teacher



* to check programme is run code and show result:
```python
if __name__ == "__main__":
    account_manager = UserAccount()

    student_profiles = [
        StudentProfile(11, 'ahmad', 'ahmad@gmail.com', '123', '123'),
        StudentProfile(12, 'hasan', 'hasan@gmail.com', '1234', '1234'),
        StudentProfile(13, 'ali', 'ali@gmail.com', '1212', '1212'),
        StudentProfile(14, 'mohammad', 'mohammad@gmail.com', '1233', '1233')
    ]

    for student_profile in student_profiles:
        account_manager.sign_up(student_profile)

    professor_profiles = [
        ProfessorProfile(21, 'dr_ahmad', 'dr_ahmad@gmail.com', '4321', '4321'),
        ProfessorProfile(22, 'dr_hasan', 'dr_hasan@gmail.com', '4322', '4322'),
        ProfessorProfile(23, 'dr_anas', 'dr_anas@gmail.com', '4333', '4333')
    ]

    professors = [
        Professor(21, 'Dr. Ahmad', 'Computer Science'),
        Professor(22, 'Dr. Hasan', 'Software Engineering'),
        Professor(23, 'Dr. Anas', 'Information Technology')
    ]

    courses = [
        Course(1911, 'C++', professors[0]),
        Course(1910, 'Java', professors[1]),
        Course(1912, 'HTML', professors[1]),
        Course(1913, 'Python', professors[2])
    ]

    for prof_profile in professor_profiles:
        account_manager.sign_up_prof(prof_profile)

    for course in courses:
        professor = next((prof for prof in professors if prof.prof_name == course.professor_name), None)
        if professor:
            professor.add_course_teach(course)

    students = [
        Student(11, 'ahmad', 'IT', 'CS'),
        Student(12, 'hasan', 'IT', 'CS'),
        Student(13, 'ali', 'IT', 'CS'),
        Student(14, 'mohammad', 'IT', 'CS')
    ]

    java_course = next((course for course in courses if course.name_course == "Java"), None)
    if java_course:
        for student in students:
            java_course.add_student(student)
            student.add_course(java_course)

    html_course = next((course for course in courses if course.name_course == "HTML"), None)
    if html_course:
        for student in students:
            html_course.add_student(student)
            student.add_course(html_course)

    while True:
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print("1. Login students")
                print("2. Login professor")
                print("3. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    email = input("Enter your email for login: ")
                    password = input("Enter your password for login: ")
                    user_id, user_name = account_manager.login(email, password)

                    if user_id:
                        profile = next((profile for profile in student_profiles if profile.id == user_id), None)
                        student = next((stu for stu in students if stu.id == user_id), None)
                        while True:
                            print('1. Go to profile')
                            print('2. Go to home')
                            print('3. Exit')
                            num = int(input('Enter your choice : '))

                            if num == 1:
                                while True:
                                    print('1. Get information')
                                    print('2. Get password')
                                    print('3. Change password ')
                                    print('4. Exit')

                                    num = int(input('Enter your choice : '))

                                    if num == 1:
                                        print(profile.get_info())
                                    elif num == 2:
                                        print(profile.get_password())
                                    elif num == 3:
                                        new_password = input("Enter your new password: ")
                                        repeat_new_password = input("Repeat your new password: ")
                                        profile.change_pass(new_password, repeat_new_password)
                                        print(profile.get_password())
                                    elif num == 4:
                                        break

                            elif num == 2:
                                while True:
                                    print('1. get student data')
                                    print('2. View courses')
                                    print('3. Add course')
                                    print('4. Remove course')
                                    print('5. Exit')
                                    choice = int(input('Enter your choice: '))

                                    if choice == 1:
                                        #student = Student(id, name, major, college)
                                        print(student.get_student_info())
                                    elif choice == 2:
                                        student.view_courses()
                                    elif choice == 3:

                                        for course in courses:
                                            print(course.get_course_info())

                                        course_id = int(input("Enter the course ID to add: "))
                                        selected_course = next(
                                            (course for course in courses if course.id_course == course_id), None)
                                        if selected_course:
                                            student.add_course(selected_course)

                                    elif choice == 4:
                                        course_id = int(input("Enter the course ID to remove: "))
                                        student.remove_course(course_id)
                                    elif choice == 5:
                                         print('Error')
                                         break
                            elif num == 3:
                                print('exit')
                                break

                elif choice == 2:
                    email = input("Enter your email for login: ")
                    password = input("Enter your password for login: ")
                    user_id, user_name = account_manager.login_prof(email, password)

                    if user_id:
                        professor = next((prof for prof in professors if prof.id_prof == user_id), None)
                        while True:
                            print('1. Go to profile')
                            print('2. Go to home')
                            print('3. Exit')
                            num = int(input('Enter your choice : '))

                            if num == 1:
                                while True:
                                    print('1. Get information')
                                    print('2. Get password')
                                    print('3. Change password ')
                                    print('4. Exit')

                                    num = int(input('Enter your choice : '))

                                    if num == 1:
                                        print(professor.get_prof_info())
                                    elif num == 2:
                                        print(professor_profiles[professors.index(professor)].get_password())
                                    elif num == 3:
                                        new_password = input("Enter your new password: ")
                                        repeat_new_password = input("Repeat your new password: ")
                                        professor_profiles[professors.index(professor)].change_pass(new_password, repeat_new_password)
                                        print(professor_profiles[professors.index(professor)].get_password())
                                    elif num == 4:
                                        break

                            elif num == 2:
                                while True:
                                    print('1. show information')
                                    print('2. View courses')
                                    print('3. View students')
                                    print('4. Exit')
                                    choice = int(input('Enter your choice: '))
                                    if choice == 1:
                                        professor.get_prof_info()
                                    elif choice == 2:
                                        professor.view_courses_teach()
                                    elif choice == 3:
                                        professor.view_students_taught()
                                    elif choice == 4:
                                        print('Exit')
                                        break
                            elif num == 3:
                                print('Exit')
                                break
                if choice == 3:
                  print('Exit...')
                  break  
        elif choice == 2:
            id = input("Enter your ID: ")
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            repeat_password = input("Repeat your password: ")


            new_profile = StudentProfile(id, name, email, password, repeat_password)
            account_manager.sign_up(new_profile)
            student_profiles.append(new_profile)
            print(f'Profile Id: {id}')
            print(f'Profile Name: {name}')
            print(f'Profile Email: {email}')
            college = input("Enter your college: ")
            major = input("Enter your major: ")

            student = Student(id, name, major, college)
            print(student.get_student_info())


        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")




```

* The result after run a program :

      1. Login
      2. Sign Up
      3. Exit
      Enter your choice:

* if choice 1 login student then :

      Enter your choice: 1
      1. Login students
      2. Login professor
      3. Exit
      Enter your choice:   

* if choice 1 then :

      Enter your email for login: 
      Enter your password for login:

* if enter email and password correct then :

      1. Go to profile
      2. Go to home
      3. Exit
      Enter your choice : 

* if choice 1 then go to profile :

      1. Get information
      2. Get password
      3. Change password 
      4. Exit
      Enter your choice : 
* if choice 2 then go to home :
          
      1. Edit data 
      2. Add course
      3. View courses
      4. Remove course
      5. Exit

* if choice 2 then :

      Enter your choice: 1
      1. Login students
      2. Login professor
      3. Exit
      Enter your choice:   

* if choice 2 then :

      Enter your email for login: 
      Enter your password for login:

* if enter email and password correct then :

      1. Go to profile
      2. Go to home
      3. Exit
      Enter your choice : 

* if choice 1 then go to profile :

      1. Get information
      2. Get password
      3. Change password 
      4. Exit
      Enter your choice : 
* 
* if choice 2 then go to home :


     1. show information
     2. View courses
     3. View students
     4. Exit
