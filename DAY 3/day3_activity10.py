student_record = []

def add_student(name, age, grade):
    new_student = (name, age, grade)
    student_record.append(new_student)

def display_students():
    print('=' * 70)
    count = 0
    for i in student_record:
        count += 1
        print(f"""
            Student #{count}
            NAME:  {i[0]}
            AGE:   {i[1]}
            GRADE: {i[2]}
            """)
    print('=' * 70)
            
run = True
while run:
    print("""
        Menu: 
        [1] - To add a record
        [2] - To display the record
        [x] - To stop
        """)
    choice = input('>> ')
    if choice == '1':
        print("""
            Enter a name, age and grade(example 'A', 'B')
        """)
        name = str(input('Name >> '))
        age = int(input('Age >> '))
        grade = str(input('Grade >> '))
        add_student(name, age, grade)
    elif choice == '2':
        display_students()
    elif choice == 'x':
        print('EXITING THE PROGRAM!!')
        break
    else:
        print("Please choose valid input.")