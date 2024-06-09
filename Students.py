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
        for course in self.courses:
            print(course.get_course_info())

    # to remove course
    def remove_course(self, course_id):
        self.courses = [course for course in self.courses if course.id_course != course_id]
        print(f"Course {course_id} removed successfully.")

    def get_student_info(self):
        return self.id, self.name, self.major, self.collage

class Course:
    def __init__(self, id_course, name_course, professor_name):
        self.id_course = id_course
        self.name_course = name_course
        self.professor_name = professor_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.id} added to course {self.id_course}.")

    def view_students(self):
        if not self.students:
            print("No students enrolled.")
        for student in self.students:
            print(student.get_student_info())

    # to get course data
    def get_course_info(self):
        return self.id_course, self.name_course, self.professor_name


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

class Professor:
    def __init__(self, id_prof, prof_name, department):
        self.id_prof = id_prof
        self.prof_name = prof_name
        self.department = department
        self.courses_taught = []

    def add_course_teach(self, course):
        self.courses_taught.append(course)
        print(f"Course {course.id_course} added to professor {self.id_prof}.")

    def remove_course_teach(self):
        for course in self.courses_taught:
            print(course.get_course_info())

    def get_prof_info(self):
        return self.id_prof, self.prof_name, self.department

if __name__ == "__main__":
    account_manager = UserAccount()



    student_profiles = [
            StudentProfile(11, 'ahmad', 'ahmad@gmail.com', '123', '123'),
            StudentProfile(12, 'hasan', 'hasan@gmail.com', '1234', '1234'),
            StudentProfile(13, 'ali', 'ali@gmail.com', '1212', '1212'),
            StudentProfile(14, 'mohahmad', 'mohahmad@gmail.com', '1233', '1233')
    ]

    for student_profile in student_profiles:
        account_manager.sign_up(student_profile)



    professor_profiles = [
        ProfessorProfile(21, 'dr_ahmad', 'dr_ahmad@gmail.com', '4321', '4321'),
        ProfessorProfile(22, 'dr_hasan', 'dr_hasan@gmail.com', '4322', '4322'),
        ProfessorProfile(23, 'dr_gfd', 'dr_gfd@gmail.com', '4333', '4333')
    ]
    for prof_profile in professor_profiles:
        account_manager.sign_up_prof(prof_profile)


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
                    #user_logged_in = account_manager.login(email, password)
                    user_id, user_name = account_manager.login(email, password)

                    if user_id:
                        profile = next((profile for profile in student_profiles if profile.id == user_id), None)
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
                                       print("Exiting...")
                                       break
                                   else:
                                       print("Invalid choice. Please try again.")

                           elif num == 2:

                               while True:

                                  print('1. Edit data')
                                  print('2. Add course')
                                  print('3. View courses')
                                  print('4. Remove course')
                                  print('5. Exit')
                                  course_choice = int(input('Enter your choice: '))

                                  if course_choice == 1:
                                      print('Profile Id :' + str(profile.id))
                                      print('Profile Name :' + profile.name)
                                      print('Profile Email :' + profile.email)
                                      collage = input("Enter your collage: ")
                                      major = input("Enter your major: ")

                                      student = Student(profile.id, profile.name, major, collage)
                                      print(student.get_student_info())

                                       #print('Student Id :' + student_profile.id)
                                       #print('Student Name :' + student_profile.name)
                                       #print('Students Email :' + student_profile.email)
                                       #collage = input("Enter your collage: ")
                                       #major = input("Enter your major: ")

                                       #student = Student(student_profile.id, student_profile.name, major, collage)
                                       #print(student.get_student_info())

                                  elif course_choice == 2:

                                      courses = [
                                         Course(1911, 'C++', 'Dr. Ahmad'),
                                         Course(1910, 'Java', 'Dr. Ali'),
                                         Course(1912, 'HTML', 'Dr. Ali'),
                                         Course(1913, 'Python', 'Dr. Anas')
                                                       ]
                                      print("Available Courses:")
                                      for course in courses:

                                          print(course.get_course_info())

                                      course_id = int(input("Enter the course ID to add: "))

                                # Find the course by ID and add to student
                                      selected_course = next((course for course in courses if course.id_course == course_id), None)
                                      if selected_course:
                                          student.add_course(selected_course)
                                      else:

                                          print("Course not found.")
                                  elif course_choice == 3:
                                       student.view_courses()
                                  elif course_choice == 4:
                                      course_id = int(input("Enter the course ID to remove: "))
                                      student.remove_course(course_id)

                                  elif course_choice == 5:
                                      print("Exiting to main menu...")
                                      break
                                  else:
                                      print("Invalid choice. Please try again.")

                           elif num == 3:

                               print('Exit...')
                               break
                           else:
                               print("Invalid choice. Please try again.")
                elif choice == 2:
                    email = input("Enter your email for login: ")
                    password = input("Enter your password for login: ")
                    # user_logged_in = account_manager.login(email, password)
                    user_id, user_name = account_manager.login_prof(email, password)
                    if user_id:
                        profile = next((profile for profile in professor_profiles if profile.id == user_id), None)
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
                                       print("Exiting...")
                                       break
                                   else:
                                       print("Invalid choice. Please try again.")
                           elif num == 2 :
                               print('this page by edit now')
                           elif num == 3:
                               print('Exit')
                               break
                           else:print("Invalid choice. Please try again.")


                elif choice == 3:
                    print('Exit....')
                    break
                else:
                    print("Invalid choice. Please try again.")


        elif choice == 2:
            id = input("Enter your ID: ")
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            repeat_password = input("Repeat your password: ")

            new_profile = StudentProfile(id, name, email, password, repeat_password)
            account_manager.sign_up(new_profile)
            student_profiles.append(new_profile)


        elif choice == 3:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

