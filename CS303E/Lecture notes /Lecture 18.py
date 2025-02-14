"""
site1 = "www.website.com"
print(site1.strip("wcom"))
print(site1.strip("."))
"""
#Q2
def calc_avg_grade(input_filename, output_filename):
    input_filen = open(input_filename, "r")
    output_filen = open(output_filename, "r")

    for line in input_file:
        split_line = line.split(": ")
        name = split_line[0]

        grades = split.line[1]      #second thing in the list 
        grades = grades.strip().split(",")  #stripping first because it's a str, not list

        for i in range(len(grades)):
            grades[i] = int(grades[i])

        avg_grade = sum(grades) / len(grades)
        print(avg_grade)

        output_file.write(f"{name}: {avg_grade:.2f}\n")

        #print("Done calculating grades") #logging

def main():
    input_filename = input("Enter a input file: ")
    calc_avg_grade(input_filename, "problem1_output.txt")
