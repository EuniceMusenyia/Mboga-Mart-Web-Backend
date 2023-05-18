# //sign-in
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

users = []

def signup():
    user = User(input("Enter username: "), input("Enter email: "), input("Enter password: "))
    users.append(user)
    print("Account created successfully")

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    for user in users:
        if  user.password == password:
            return"Login successful"
            
    return"Invalid  password"
    
   