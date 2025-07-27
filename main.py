class student:

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display_info(self):
        print(f"Name = {self.name}")
        print(f"Roll No = {self.rollno}")
        print(f"Marks = {self.marks}")

    def cal_avg(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print(f"Total marks = {total}")
        print(f"Average Marks = {avg}")

    def saving_user_data(self):
        with open("saves.txt","a") as file:
            file.write(f"Name : {self.name}\n")
            file.write(f"Roll No : {self.rollno}\n")
            file.write(f"Marks : {self.marks}\n")
    
def validating_input():
        
    while True:
        name = input("Enter the name : ").strip()
        if not name.isalpha():
            print("Invalid name ,the name must contain only alphabets in it")
            continue
        
        try:
            rollno = int(input("Enter the Roll No : "))
        except ValueError:
            print("Invalid Roll number")
            continue

        try:
            marks_input = input("Enter the marks(seperated by comma)")
            marks =[int(m.strip())for m in marks_input.split(",")]

        except ValueError:
            print("marks must be integer seperated by comma")
            continue

        return student(name,rollno,marks)
        
def search_student(students,rollno):
    for student in students:
        if student.rollno == rollno:
            print("student found")
            student.display_info()
            return student
            
    print("Student not found")
    return None
        
def update_marks(student):
    try:
        new_marks_input = input("Enter the updated marks : ")
        new_marks = [int(m.strip())for m in new_marks_input.split(",")]
        student.marks = new_marks
        print("Update marks")
        
    except ValueError:
        print("Invalid Marks Format")

def main_menu():
    students = []

    while True:
        print("\n Student Marks Management System")
        print("1.  Add student")
        print("2.  Search student by roll number")
        print("3.  Update student marks")
        print("4.  Display all students")
        print("5.  Save all data to file")
        print("6.  Exit")

        choice = input("Enter your choice(1-6) : ")
       

        if choice == "1":
            student = validating_input()
            students.append(student)
            print("student added!")

        elif choice == "2":
            try:
                rollno = int(input("Enter the roll no to search : "))
                search_student(students,rollno)
            except ValueError:
                print("Invalid roll number")

        elif choice == "3":
            try:
                rollno = int(input("Enter the roll no to search : "))
                found_student = search_student(students, rollno)
                if found_student:
                    update_marks(found_student)
               
            except ValueError:
                print("Invalid output")

        elif choice == "4":
            rollno = int(input("Enter the roll no to search : "))
            if not students:
                print("No students found")
                continue
            for s in students:
                s.display_info()
                s.cal_avg()


        elif choice == "5":
            for s in students:
                s.saving_user_data()
            print("All student data saved to 'saves.txt")

        elif choice == "6":
            print("Exiting... Have a great day!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 6.")


# Add a student
s1 = validating_input()
student.append(s1)
s1.display_info()
s1.cal_avg()
s1.saving_user_data()

# Search by roll no
search_student(student, int(input("Enter roll no to search: ")))

# Update marks
update_marks(s1)
s1.display_info()

# another student

s2 = validating_input()
student.append(s1)
s2.display_info()
s2.cal_avg()
s2.saving_user_data()

# Search by roll no
search_student(student, int(input("Enter roll no to search: ")))

# Update marks
update_marks(s2)
s1.display_info()
