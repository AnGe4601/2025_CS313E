#Q1
def count_grades(final_grades):
    grade_count = {}
    #reading the file into py
    #for name in final_grades:
        #final_grades[name]
    for name, grades in final_grades.item():
        if grade not in grade_count:
            grade_count[grade] = 1
        else:
            grade_count[grade] += 1

        return grade_count

def main:
    grade_book = {
        'Ana' : 90,
        'Bob' : 88,
        'Cam' : 95,
        'Dee' : 90,
        'Eve' : 90
        }
    print(count_grade(final_grades)

main()

#Q2
file = open('cities.txt', 'r')
contents = file.readline()
while contents != '':
    print('Lines:', contents.strip())
    contents = file.readline()

#for line in file:
    #print('Line:", line.strip())
#for loop will automatically read file for you

file.close()
