#Older version of code
"""
import csv

students=[]
with open('students.csv') as file:
        reader=csv.DictReader(file)
        for row in reader:
            students.append({"name":row["name"], "address": row["address"]})
'''
        name, address=line.rstrip().split(",")
        student={"name":name , "address":address}
        students.append(student)
'''


#Another way of getting the name

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{(student['name']).title()} is from {(student['address']).title()}")
"""

#Start Fresh
import csv

name=input("What\'s your name ")
home=input("Where\'s your home ")

with open("students.csv", "a") as file:
    writer=csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home":home, "name":name})

