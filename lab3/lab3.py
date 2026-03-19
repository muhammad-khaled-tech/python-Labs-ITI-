import os 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, ".database")
STUDENTS_PATH = os.path.join(DB_DIR, "students.txt")
GRADES_PATH = os.path.join(DB_DIR, "grades.txt")

#========================================================

def init_students_database():
    if not os.path.exists(DB_DIR):
        os.mkdir(DB_DIR)
        print(f"intilized the databse at folder {DB_DIR}")
    f=open(STUDENTS_PATH, "w")
    f.write("1,mohamed khaled\n2,zeyad hisham\n3,moahmed abdelhaq\n")
    f.close()
    f=open(GRADES_PATH , "w")
    f.write("1,python,85\n2,java,90\n3,cpp,100\n")
    f.close()
    print(f"done making the students.txt at {STUDENTS_PATH} and grades.txt at {GRADES_PATH}")


def display_all_students():
    f=open(STUDENTS_PATH , "r")
    for line in f:
        parts=line.strip().split(',') 
        print(f"--> {parts[1]}")
    f.close()    
    

def join_tables():
    student_dict ={}
    f = open(STUDENTS_PATH , "r") 
    for line in f:
        studentID,name=line.strip().split(',')
        student_dict[studentID]=name
    f.close()
    return student_dict     
        
    

def display_grades(subject=""):
    grades=open(GRADES_PATH,"r")
    found=False
    students_map=join_tables()
    subject=subject.lower()
    print(f"=============== Report for: {subject if subject else "All subjects"} ==================") 
    for line in grades:
        studentID , sub , grade=line.lower().strip().split(',')
        if subject=="" :
            student_name = students_map.get(studentID , "unknown student")
            print(f"Name: {student_name:<18} | subject: {sub:<7} | Grade: {grade:<3}")
            found=True
        elif subject == sub:
            student_name = students_map.get(studentID , "unknown student")
            print(f"Name: {student_name:<18} | Grade: {grade:<3}")
            found=True
        
    if not found:
        print(f"no students with this {subject} :)")
    print("=====================================================") 
    grades.close()
    

def student_report_and_average():
    student_map = join_tables()
    
    while True:
        search_id = input("Please enter the student ID (or '000' to exit): ").strip()
        
        if search_id == "000":
            print("Bye bye ... ")
            return
            
        if search_id not in student_map:
            print(" There is no student with this ID, please try again.")
        else:
            break 
    
    print(f"\n=============== Report for: {student_map[search_id]} ==================") 
    print(f"ID: {search_id:<4} | Name: {student_map[search_id]:<18}")
    print("-" * 45)
    
    total_sum = 0
    subjects_count = 0 
    
    grades = open(GRADES_PATH, "r")
    for line in grades:
        sid, sub, grade = line.strip().lower().split(',')
        
        if sid == search_id:
            total_sum += float(grade)
            subjects_count += 1 
            print(f"Subject: {sub:<10} | Grade: {grade:<4}")
            
    grades.close()
    
    print("=" * 45)
    if subjects_count > 0:
        average = total_sum / subjects_count
        print(f"AVERAGE of grades: {average:.2f}")     
    else:
        print("This student has no recorded grades yet.")  
        
   
def add_new_student():
    print("\n--- Add New Student ---")
    student_map = join_tables() 
    new_id = input("Enter new Student ID: ").strip()
    if new_id in student_map:
        print(f" Error: Student ID '{new_id}' already exists for ({student_map[new_id]}).")
        return     
    new_name = input("Enter Student Name: ").strip()
    f = open(STUDENTS_PATH, "a")
    f.write(f"{new_id},{new_name}\n")
    f.close()
    print(f"Success: Student '{new_name}' added successfully!")


def add_new_student():
    print("\n--- Add New Student ---")
    student_map = join_tables() 
    if not student_map: 
        new_id = "1"
    else:
        max_id = max(int(sid) for sid in student_map.keys())
        new_id = str(max_id + 1)   
    print(f"Auto-generated Student ID: {new_id}")
    new_name = input("Enter Student Name: ").strip()
    f = open(STUDENTS_PATH, "a")
    f.write(f"{new_id},{new_name}\n")
    f.close()
    print(f"Success: Student '{new_name}' added successfully with ID ({new_id})!")
    
def add_new_grade():
    print("\n--- Add New Grade ---")
    student_map = join_tables()
    student_id = input("Enter Student ID: ").strip()
    if student_id not in student_map:
        print(f"Error: No student found with ID '{student_id}'. Please add the student first.")
        return  
    subject = input("Enter Subject Name: ").strip().lower()
    grade = input("Enter Grade: ").strip()
    f = open(GRADES_PATH, "a")
    f.write(f"{student_id},{subject},{grade}\n")
    f.close()
    print(f" Success: Grade added for '{student_map[student_id]}' in {subject}!")  
   
        
def main():
    while True:
        os.system('clear') #  i searched for it and it is a system call for command clear or cls
        print("\n" + "="*45)
        print(" Student Management System ".center(45))
        print("="*45)
        print("1. Initialize Database (Reset files)")
        print("2. Display All Students")
        print("3. Display Grades for a Subject (or All)")
        print("4. Get Student Transcript & Average")
        print("5. Add New Student") 
        print("6. Add New Grade")   
        print("0. Exit")
        print("="*45)
        
        choice = input("Enter your choice (0-6): ").strip() 
        
        if choice in ["2", "3", "4", "5", "6"]:
            if not os.path.exists(STUDENTS_PATH) or not os.path.exists(GRADES_PATH):
                print("\nError: Database files not found!")
                print("Please initialize the database first by selecting option '1'.")
                input("\n Press Enter to continue...")
                continue
        
        if choice == "1":
            print("\n Initializing...")
            init_students_database()     
        elif choice == "2":
            print("\n All Students:")
            display_all_students() 
        elif choice == "3":
            subject = input("\nEnter subject name (or press Enter for all): ").strip()
            display_grades(subject)
        elif choice == "4":
            print("\n Search Student...")
            student_report_and_average()
        elif choice == "5":
            add_new_student()
        elif choice == "6":
            add_new_grade()
        elif choice == "0":
            print("\nExiting program. Goodbye! \n")
            break
        else:
            print("\n Invalid choice. Please enter a number between 0 and 6.")
        
        if choice != "0":
            input("\n Press Enter to go back to the menu...")

main()    

        

        
            
        
