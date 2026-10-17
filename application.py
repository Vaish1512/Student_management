students = []

def add_student(name, roll_no, email):
    students.append({
        "name": name,
        "roll_no": roll_no,
        "email": email
    })

def display_students():
    for s in students:
        print(s["roll_no"], s["name"], s["email"])

add_student("Ravi", 101, "ravi@gmail.com")
display_students()