import random
import secrets
import string
def generate_password():
    password_length=random.randint(8, 16)
    password_list=[]
    while password_length>len(password_list):
        password_character=secrets.choice((string.punctuation+string.digits+string.ascii_letters))
        password_list.append(password_character)
    password="".join(password_list)
    print(password)
    another_password=input("do you want to generate another password? ")
    if another_password=="yes":
        generate_password()
    elif another_password=="no":
        main()
    else:
        print("invalid input")



def main():
    choice=input("do you want to generate a password? ")
    while True:
        if choice=="yes":
            generate_password()
        elif choice=="no":
            break
        else:
            print("invalid choice")
if __name__=="__main__":
    main()