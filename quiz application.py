import json

from soupsieve.util import lower


def display():
    print(''' 
    ============Quiz==============
               WELCOME
    this application is designed to 
    ask a couple of questions 
    and save your response and give you
    a final score
         
        Options
    ''')
    print('''
    1. Start quiz
    2. View results
    3. View answers
    4. Save
    5. Exit
    ''')

marks=[]
def start_quiz():
    question_1=lower(input("What is the capital city of France?: "))
    if question_1.capitalize()=="Paris":
        print("Correct!!")
        marks.append(10)
    else:
        print("Incorrect answer")

    question_2 = lower(input("Which planet is known as the red planet?: "))
    if question_2.capitalize() == "Mars":
        print("Correct!!")
        marks.append(10)
    else:
        print("Incorrect answer")

    question_3 = lower(input("Who wrote the play Romeo and Juliet?: "))
    if question_3== "william shakespear":
        print("Correct!!")
        marks.append(10)
    else:
        print("Incorrect answer")

    question_4 = lower(input("What is the largest ocean on earth?: "))
    if question_4 == "pacific ocean":
        print("Correct!!")
        marks.append(10)
    else:
        print("Incorrect answer")

    question_5 = input("In what year did the titanic sink?: ")
    if question_5 == "1912":
        print("Correct!!")
        marks.append(10)
    else:
        print("Incorrect answer")
    Marks()
    save()




def Marks():
    if not marks:
        print("There are no marks to display")
        return
    results=sum(marks)
    print (f"You scored {results}/50")


def answers():
    print('''
         question 1.Paris
         question 2.Mars
         question 3.William Shakespear
         question 4.Pacific Ocean
         question 5.1912
         
    
    ''')


def save():
    with open("marks.json", "w") as file:
        json.dump(marks, file)
    print("marks saved successfully")

def load():
    global marks
    try:
        with open("marks.json", "r") as file:
            quiz=json.load(file)
    except FileNotFoundError:
        marks=[]
        print("marks loaded successfuly")






def main():
    load()
    while True:
        display()
        choice=input("What would you like to do? ")
        if choice=="1":
            start_quiz()
        elif choice=="2":
            Marks()
        elif choice=="3":
            answers()
        elif choice=="4":
            save()
        elif choice=="5":
            break
        else:
            print("Invalid choice")
    print("Thank you for playing")


if __name__=="__main__":
    main()




