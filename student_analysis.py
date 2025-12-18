# -------------------------
# PART 1: Data Collection
# -------------------------

# Department information stored in a tuple
dept_info = (
    "Department of Medicine",
    "Faculty of Clinical Sciences",
    2025
)

# Students dictionary with at least 5 students
students = {
    "Nimat Okikiola Olaleye": {
        "name": "Nimat Okikiola Olaleye",
        "matric": "22/48KC124",
        "age": 22,
        "cgpa": 4.26,
        "is_active": True,
        "courses": ["General Course", "Anatomy"],
        "grades": {
            "General Course": "A",
            "Anatomy": "A"
        },
        "outstanding_courses": 0
    },
    "Adebayo Tunde": {
        "name": "Adebayo Tunde",
        "matric": "22/48KC130",
        "age": 23,
        "cgpa": 3.58,
        "is_active": True,
        "courses": ["Physiology", "Medical Biochemistry"],
        "grades": {
            "Physiology": "B",
            "Medical Biochemistry": "B"
        },
        "outstanding_courses": 0
    },
    "Lawal Zainab": {
        "name": "Lawal Zainab",
        "matric": "22/48KC141",
        "age": 21,
        "cgpa": 3.02,
        "is_active": True,
        "courses": ["Anatomy", "Physiology"],
        "grades": {
            "Anatomy": "C",
            "Physiology": "B"
        },
        "outstanding_courses": 1
    },
    "Okorie Chibuzo": {
        "name": "Okorie Chibuzo",
        "matric": "22/48KC156",
        "age": 24,
        "cgpa": 2.74,
        "is_active": True,
        "courses": ["Medical Biochemistry", "Integrated Paper"],
        "grades": {
            "Medical Biochemistry": "C",
            "Integrated Paper": "D"
        },
        "outstanding_courses": 1
    },
    "Sadiq Mariam": {
        "name": "Sadiq Mariam",
        "matric": "22/48KC168",
        "age": 23,
        "cgpa": 4.61,
        "is_active": True,
        "courses": ["General Course", "Integrated Paper"],
        "grades": {
            "General Course": "A",
            "Integrated Paper": "A"
        },
        "outstanding_courses": 0
    }
}

# Create list of student names
student_names = list(students.keys())

# Create set of unique courses
unique_courses = set()
for profile in students.values():
    unique_courses.update(profile["courses"])

students, dept_info, student_names, unique_courses
# -------------------------
# PART 2: Functions
# -------------------------

def display_students(students):
    print("\n--- STUDENT RECORDS ---")
    for info in students.values():
        print(f"Name: {info['name']}")
        print(f"Matric No: {info['matric']}")
        print(f"Age: {info['age']}")
        print(f"CGPA: {info['cgpa']}")
        print(f"Active Status: {info['is_active']}")
        print(f"Courses: {', '.join(info['courses'])}")
        print("-" * 40)


def add_student(students):
    print("\n--- ADD NEW STUDENT ---")
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    age = int(input("Enter age: "))
    cgpa = float(input("Enter CGPA: "))

    courses = input("Enter courses (separate with comma): ").split(",")
    courses = [course.strip() for course in courses]

    students[name] = {
        "name": name,
        "matric": matric,
        "age": age,
        "cgpa": cgpa,
        "is_active": True,
        "courses": courses,
        "grades": {},
        "outstanding_courses": 0
    }

    print("Student successfully added.")


def check_eligibility(students):
    print("\n--- GRADUATION ELIGIBILITY ---")
    for info in students.values():
        if info["cgpa"] >= 2.0 and info["outstanding_courses"] == 0:
            status = "Eligible"
        else:
            status = "Not Eligible"
        print(f"{info['name']} → {status}")


def best_performer(students):
    top_student = max(students.values(), key=lambda x: x["cgpa"])
    print("\n--- BEST PERFORMING STUDENT ---")
    print(f"Name: {top_student['name']}")
    print(f"CGPA: {top_student['cgpa']}")
  # -------------------------
# PART 3: Menu System
# -------------------------

def main_menu(students):
    while True:
        print("\n===== STUDENT ACADEMIC RECORD SYSTEM =====")
        print("1. View all students")
        print("2. Add a new student")
        print("3. Check graduation eligibility")
        print("4. View best performing student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_students(students)

        elif choice == "2":
            add_student(students)

        elif choice == "3":
            check_eligibility(students)

        elif choice == "4":
            best_performer(students)

        elif choice == "5":
            print("Exiting the system... Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")
          # -------------------------
# PART 4: Conditions & Logic
# -------------------------

def academic_status(students):
    print("\n--- ACADEMIC STATUS REPORT ---")
    for info in students.values():
        if info["is_active"]:
            status = "Active Student"
        else:
            status = "Inactive Student"

        if info["cgpa"] < 2.0:
            standing = "At Risk"
        else:
            standing = "Good Standing"

        print(f"{info['name']} → {status} | {standing}")
      # -------------------------
# PART 5: Run the System
# -------------------------

main_menu(students)
