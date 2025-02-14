class Student:
    def __init__(self, name, ID, major):
        self.name = name
        self.ID = ID
        self.major = major
        self.__course_codes = list()
        self.__course_grades = {}
        
    def get_course_codes(self):
        return self.__course_codes
    
    def get_course_grade(self, course_grade):
        return sefl.__course_grades[course_grade]
    
    def set_major(self, new_major):
        self.major = new_major

    def add_course(self, course_code):
        self.__course_codes.append(course_code)
        self.__course_grades[course_code] = ""
           
    def remove_course(self, course_code):
        if course_code in self.__course_code:
            self.__course_codes.remove(course_code)
            del self.__course_grades[course_code]
    
    def update_course_grade(self, course_code, grade):
        if course_code in self.__course_grades:
            self.__course_grades[course_code] = grade
        '''    
        if self.__course_grades != "":
            print("already taken")
        else:
            self.__course_grades[course_code] = grade
        '''    
    def __str__(self):  # converting all the info in the class into str 
        return f"Student: {self.name} ({self.ID})\nMajor: {self.major}"

#class Course:
    #def __init__:

def main():
    me = Student("Angela", "97695148", "Studio Art")
    print(me)
    
main() 
        
