name = str(input('Enter a name > ')).capitalize()
math = float(input('Enter grade for math > '))
science = float(input('Enter grade for science > '))
english = float(input('Enter grade for english > '))

average = (math + science + english ) / 3
print(f"""
        Name: {name}
        Math: {math}
        Science: {science}
        English: {english}
        Average: {average}
        """)

msg = ''
if math < 75:
    msg += 'Math '
if english < 75:
    msg += 'English'
if science < 75:
    msg += ' Science'

if average >= 75:
    if msg:
        print(f'Congratulations! You passed the semester. But you need to re-enroll {msg} subject')
    else:
        print(f'Congratulations! You passed the semester.')
else:
    print(f'Sorry, You failed the semester')

