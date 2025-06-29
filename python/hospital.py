import sqlite3

# This creates a new database file called "database.db"
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# This creates a table to store patient details
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    diagnosis TEXT NOT NULL
)
''')

conn.commit()


def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (M/F): ")
    diagnosis = input("Enter diagnosis: ")

    cursor.execute("INSERT INTO patients (name, age, gender, diagnosis) VALUES (?, ?, ?, ?)",
                   (name, age, gender, diagnosis))
    conn.commit()
    print("✅ Patient added successfully!\n")


def view_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("⚠️ No patient records found.\n")


def search_patient():
    pid = input("Enter patient ID to search: ")
    cursor.execute("SELECT * FROM patients WHERE id=?", (pid,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("❌ Patient not found.\n")

def update_patient():
    pid = input("Enter patient ID to update: ")
    name = input("New name: ")
    age = int(input("New age: "))
    gender = input("New gender: ")
    diagnosis = input("New diagnosis: ")

    cursor.execute("UPDATE patients SET name=?, age=?, gender=?, diagnosis=? WHERE id=?",
                   (name, age, gender, diagnosis, pid))
    conn.commit()
    print("🔄 Patient updated successfully!\n")


def delete_patient():
    pid = input("Enter patient ID to delete: ")
    cursor.execute("DELETE FROM patients WHERE id=?", (pid,))
    conn.commit()
    print("🗑️ Patient deleted successfully!\n")


def menu():
    while True:
        print("\n--- Hospital Patient Management ---")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search by Patient ID")
        print("4. Update Patient Details")
        print("5. Delete Patient")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            break
        else:
            print("❗Invalid option. Try again.")

menu()
conn.close()





