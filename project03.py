'''you are building a small program for a school
the user must enter the students name and marks in three subjects
the program should calculate the total,average, and display a grade
if marks are not between 0 and 100 , show error message'''

stu_name = input("enter student name: ")

mark1 = int(input("enter marks in first sub: "))
mark2 = int(input("enter marks in second sub: "))
mark3 = int(input("enter marks in third sub: "))

if (0>mark1 or mark1>100 or 0>mark2 or mark2>100 or 0>mark3 or mark3>100):
    print("ERROR!! Please input correct marks")
else:
    total_marks = mark1 + mark2 + mark3
    print(f"total marks = {total_marks}")

    avg = (mark1+mark2+mark3)/3
    print(f"average marks = {avg}")

    if avg>90:
        print("GRADE A")

    elif 90>avg>75:
        print("GRADE B")

    else:
        print("GRADE C")