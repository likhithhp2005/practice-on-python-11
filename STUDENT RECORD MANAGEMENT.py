import os

file_name = "students.txt"

if not os.path.exists(file_name):
    open(file_name, "w").close()

while True:
    print("\n========== STUDENT RECORD MANAGEMENT ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Backup File")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        sem = input("Enter Semester: ")
        cgpa = input("Enter CGPA: ")

        file = open(file_name, "a")
        file.write(usn + "," + name + "," + dept + "," + sem + "," + cgpa + "\n")
        file.close()

        print("Student record added successfully.")

    elif choice == "2":
        file = open(file_name, "r")
        records = file.readlines()
        file.close()

        if len(records) == 0:
            print("No records found.")
        else:
            print("\nUSN\t\tNAME\t\tDEPT\tSEM\tCGPA")
            print("-" * 60)
            for record in records:
                usn, name, dept, sem, cgpa = record.strip().split(",")
                print(usn, "\t", name, "\t", dept, "\t", sem, "\t", cgpa)

    elif choice == "3":
        search = input("Enter USN to search: ")
        found = False

        file = open(file_name, "r")
        for line in file:
            usn, name, dept, sem, cgpa = line.strip().split(",")
            if usn == search:
                print("\nStudent Found")
                print("USN:", usn)
                print("Name:", name)
                print("Department:", dept)
                print("Semester:", sem)
                print("CGPA:", cgpa)
                found = True
                break
        file.close()

        if not found:
            print("Student not found.")

    elif choice == "4":
        search = input("Enter USN to update: ")

        file = open(file_name, "r")
        records = file.readlines()
        file.close()

        file = open(file_name, "w")
        updated = False

        for line in records:
            usn, name, dept, sem, cgpa = line.strip().split(",")

            if usn == search:
                name = input("Enter New Name: ")
                dept = input("Enter New Department: ")
                sem = input("Enter New Semester: ")
                cgpa = input("Enter New CGPA: ")
                updated = True

            file.write(usn + "," + name + "," + dept + "," + sem + "," + cgpa + "\n")

        file.close()

        if updated:
            print("Record updated successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        search = input("Enter USN to delete: ")

        file = open(file_name, "r")
        records = file.readlines()
        file.close()

        file = open(file_name, "w")
        deleted = False

        for line in records:
            usn, name, dept, sem, cgpa = line.strip().split(",")

            if usn != search:
                file.write(line)
            else:
                deleted = True

        file.close()

        if deleted:
            print("Record deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        file = open(file_name, "r")
        count = len(file.readlines())
        file.close()
        print("Total Students:", count)

    elif choice == "7":
        source = open(file_name, "r")
        data = source.read()
        source.close()

        backup = open("backup_students.txt", "w")
        backup.write(data)
        backup.close()

        print("Backup created successfully.")

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid choice.")