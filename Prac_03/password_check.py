def main():
    password = input("Enter your password: ")
    new_password = get_password(password)
    print(new_password)

def get_password(password):
    new_password = ""
    for x in range(len(password)):
       new_password = new_password + "*"
    return new_password
main()