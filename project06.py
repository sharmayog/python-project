'''a company needs a program that reads employee names and their basic salary.
The program should: Calculate total salary including HRA(house rent allowance) (20%) and
 DA (dearness allowance) (10%).
Stop taking input when the user types "stop". Display each employees total salary at the end.
Concepts: while loop, arithmetic operations, condition check, formatted output.'''

while True:
    name = int(input("enter basic1 salary: "))

    if name == "stop":
        break
    salary = int(input("enter basic2 salary: "))
    hra = salary*0.20
    da = salary*0.10
    total_salary = salary + hra + da
    print(f"{name}s total salary:{total_salary}")
