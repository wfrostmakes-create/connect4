
import passwords

username = input("Username: ")
password = input("Password: ")

if passwords.login(username, password):
    print("Login successful!")


else:
    print("Access denied!")
