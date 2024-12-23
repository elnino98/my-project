class UserAccount:
    def __init__(self):
        self.users = []

    def sign_up(self, profile):
        return self._sign_up(profile, "student")

    def sign_up_prof(self, profile):
        return self._sign_up(profile, "professor")

    def _sign_up(self, profile, user_type):
        name = profile.name
        email = profile.email
        password = profile.password
        repeat_password = profile.repeat_password

        if not name.strip() or not email.strip() or not password.strip() or not repeat_password.strip():
            print("Please fill in all the fields.")
            return False

        if any(user['email'] == email for user in self.users):
            print("Email already exists. Please use a different email.")
            return False

        if password != repeat_password:
            print("Passwords do not match.")
            return False

        self.users.append({'id': profile.id, 'name': name, 'email': email, 'password': password, 'type': user_type})
        #print("Account created successfully.")
        return True

    def login(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                print("Login successful.")
                return user['id'], user['name']
        print("Invalid email or password.")
        return None, None

    def login_prof(self, email, password):
        return self.login(email, password)


class StudentProfile:
    def __init__(self, id, name, email, password, repeat_password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

    def get_info(self):
        return self.id, self.name, self.email

    def get_password(self):
        return self.password

    def change_pass(self, new_pass, repeat_new_pass):
        if new_pass != repeat_new_pass:
            print("New passwords do not match.")
            return False
        self.password = new_pass
        print("Password changed successfully.")
        return True


class ProfessorProfile:
    def __init__(self, id, name, email, password, repeat_password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

    def get_info(self):
        return self.id, self.name, self.email

    def get_password(self):
        return self.password

    def change_pass(self, new_pass, repeat_new_pass):
        if new_pass != repeat_new_pass:
            print("New passwords do not match.")
            return False
        self.password = new_pass
        print("Password changed successfully.")
        return True


class Student:
    def __init__(self, id, name, major, college):
        self.id = id
        self.name = name
        self.major = major
        self.courses = []
        self.college = college

    def add_course(self, course):
        self.courses.append(course)
        #print(f"Course {course.id_course} added successfully.")

    def view_courses(self):
        if not self.courses:
            print("No courses added.")
        else:
            for course in self.courses:
                print(course.get_course_info())

    def remove_course(self, course_id):
        self.courses = [course for course in self.courses if course.id_course != course_id]
        #print(f"Course {course_id} removed successfully.")

    def get_student_info(self):
        return self.id, self.name, self.major, self.college


class Professor:
    def __init__(self, id_prof, prof_name, department):
        self.id_prof = id_prof
        self.prof_name = prof_name
        self.department = department
        self.courses_taught = []

    def add_course_teach(self, course):
        self.courses_taught.append(course)
        #print(f"Course {course.id_course} added to professor {self.id_prof}.")

    def view_courses_teach(self):
        for course in self.courses_taught:
            print(course.get_course_info())

    def view_students_taught(self):
        for course in self.courses_taught:
            print(f"Course {course.id_course}:")
            course.view_students()

    def get_prof_info(self):
        return self.id_prof, self.prof_name, self.department


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
                                        print(professor.get_prof_info())
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


