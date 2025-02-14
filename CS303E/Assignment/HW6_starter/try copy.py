input_file = open('input.txt', "r")

for line in input_file:
    line = line.split(": ")
    city = line[0]
    temps = line[1].strip()
    temps = temps.split(", ")
print(temp) 

input_file.close()
