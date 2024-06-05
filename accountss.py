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



class Student_profile:
    def __init__(self,id,name,email,password,repeat_password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password


    # to get information of student
    def get_info(self):
        return self.id , self.name , self.email

    # to get password
    def get_password(self):
        return self.password

    # to change password
    def change_pass(self , new_pass):
        self.password = new_pass


if __name__ == "__main__":
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




    #print(student_profile.get_info())


