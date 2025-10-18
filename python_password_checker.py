import re
#password check conditions
#min 8 charecters
def check_password_strength(password):
    if len(password)<8:
        return "Wrong: passwprd must be atleast of 8chars"
    if not any(char.isdigit() for char in password):
        return "Wrong: password must contain atlest 1 digit"
    if not any(char.isupper() for char in password):
        return "Wrong: password must contain atleast 1 uppercase"
    if not any(char.islower() for char in password ):
        return "Wrong: password must contain atleast 1 lowercase"
    if not re.search(r'[~`!@#$%^&*()_\-+={}[\]|\\:;"\'<>,.?/]', password):
        print("Medium: Password must include at least one special character")
        
    return "Your password is strong"

def password_checker():
    print("Welcome to the password strength checker")
    while True:
        password=input("enter your password(or type 'exit' or 'quit'):")
        if password.lower()=='exit':
            print("thank you for using this tool")
            break
        result =check_password_strength(password)
        print(result)
        
#run the password checker tool
if __name__=="__main__":
    password_checker()
