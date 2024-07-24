class Student:
    ...
def main():
    Student=get_student()
    print(f"{Student.name} from {Student.house}")

def get_student():
    stdnt=Student()
    stdnt.name=input("Name: ")
    stdnt.house=input("House: ")
    return stdnt


if __name__=="__main__":
    main()
