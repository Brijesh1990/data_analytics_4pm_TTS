"""
Student Management System - Console Version
-------------------------------------------
Single-file Python application using SQLite.

Features:
1. Create, read, update and delete student records.
2. Mark student attendance by date (Present / Absent).
3. Display attendance summary in a Matplotlib pie chart.

Install:
    pip install matplotlib

Run:
    python app.py

The SQLite database file is created automatically:
    student_management.db
"""

import sqlite3
from datetime import date, datetime

import matplotlib.pyplot as plt


DB_NAME = "student_management.db"


class StudentManagementSystem:
    def __init__(self, database_name=DB_NAME):
        # Connect to SQLite. The database is created if it does not exist.
        self.conn = sqlite3.connect(database_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        """Create students and attendance tables."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    course TEXT NOT NULL
                )
            """)

            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS attendance (
                    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    attendance_date TEXT NOT NULL,
                    status TEXT NOT NULL
                        CHECK(status IN ('Present', 'Absent')),
                    UNIQUE(student_id, attendance_date),
                    FOREIGN KEY(student_id)
                        REFERENCES students(student_id)
                        ON DELETE CASCADE
                )
            """)

    # -------------------- STUDENT CRUD --------------------

    def add_student(self):
        print("\n--- Add Student ---")
        name = input("Enter student name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone: ").strip()
        course = input("Enter course: ").strip()

        if not name or not course:
            print("Error: Student name and course are required.")
            return

        try:
            with self.conn:
                cursor = self.conn.execute("""
                    INSERT INTO students (name, email, phone, course)
                    VALUES (?, ?, ?, ?)
                """, (name, email, phone, course))
            print(f"Student added successfully. Student ID: {cursor.lastrowid}")
        except sqlite3.Error as error:
            print("Database error:", error)

    def view_students(self):
        print("\n--- Student Records ---")
        rows = self.conn.execute("""
            SELECT student_id, name, email, phone, course
            FROM students
            ORDER BY student_id
        """).fetchall()

        if not rows:
            print("No student records found.")
            return

        print("-" * 105)
        print(f"{'ID':<6}{'NAME':<24}{'EMAIL':<30}{'PHONE':<17}{'COURSE':<25}")
        print("-" * 105)

        for student_id, name, email, phone, course in rows:
            print(
                f"{student_id:<6}{name[:22]:<24}{(email or '-')[:28]:<30}"
                f"{(phone or '-')[:15]:<17}{course[:23]:<25}"
            )
        print("-" * 105)

    def update_student(self):
        print("\n--- Update Student ---")
        self.view_students()

        try:
            student_id = int(input("Enter student ID to update: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        student = self.conn.execute("""
            SELECT name, email, phone, course
            FROM students
            WHERE student_id = ?
        """, (student_id,)).fetchone()

        if student is None:
            print("Student not found.")
            return

        print("Press Enter to keep the current value.")
        name = input(f"Name [{student[0]}]: ").strip() or student[0]
        email = input(f"Email [{student[1] or ''}]: ").strip() or student[1]
        phone = input(f"Phone [{student[2] or ''}]: ").strip() or student[2]
        course = input(f"Course [{student[3]}]: ").strip() or student[3]

        try:
            with self.conn:
                self.conn.execute("""
                    UPDATE students
                    SET name = ?, email = ?, phone = ?, course = ?
                    WHERE student_id = ?
                """, (name, email, phone, course, student_id))
            print("Student updated successfully.")
        except sqlite3.Error as error:
            print("Database error:", error)

    def delete_student(self):
        print("\n--- Delete Student ---")
        self.view_students()

        try:
            student_id = int(input("Enter student ID to delete: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        student = self.conn.execute(
            "SELECT name FROM students WHERE student_id = ?",
            (student_id,)
        ).fetchone()

        if student is None:
            print("Student not found.")
            return

        confirm = input(
            f"Delete '{student[0]}' and their attendance records? (y/n): "
        ).strip().lower()

        if confirm != "y":
            print("Delete cancelled.")
            return

        try:
            with self.conn:
                self.conn.execute(
                    "DELETE FROM students WHERE student_id = ?",
                    (student_id,)
                )
            print("Student and related attendance records deleted.")
        except sqlite3.Error as error:
            print("Database error:", error)

    # -------------------- ATTENDANCE --------------------

    def mark_attendance(self):
        print("\n--- Mark Attendance ---")
        self.view_students()

        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        exists = self.conn.execute(
            "SELECT 1 FROM students WHERE student_id = ?",
            (student_id,)
        ).fetchone()

        if not exists:
            print("Student not found.")
            return

        attendance_date = input(
            f"Enter date (YYYY-MM-DD) [default: {date.today()}]: "
        ).strip()
        if not attendance_date:
            attendance_date = date.today().isoformat()

        try:
            # Validate date format and actual calendar date.
            attendance_date = datetime.strptime(
                attendance_date, "%Y-%m-%d"
            ).date().isoformat()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, for example 2026-11-03.")
            return

        print("1. Present")
        print("2. Absent")
        choice = input("Choose attendance status: ").strip()

        status_map = {"1": "Present", "2": "Absent"}
        status = status_map.get(choice)

        if status is None:
            print("Invalid choice.")
            return

        try:
            # If this student/date already exists, update its status.
            with self.conn:
                self.conn.execute("""
                    INSERT INTO attendance (student_id, attendance_date, status)
                    VALUES (?, ?, ?)
                    ON CONFLICT(student_id, attendance_date)
                    DO UPDATE SET status = excluded.status
                """, (student_id, attendance_date, status))
            print(f"Attendance saved: {status} on {attendance_date}.")
        except sqlite3.Error as error:
            print("Database error:", error)

    def view_attendance(self):
        print("\n--- Attendance Records ---")
        rows = self.conn.execute("""
            SELECT a.attendance_id, s.student_id, s.name,
                   a.attendance_date, a.status
            FROM attendance AS a
            INNER JOIN students AS s ON s.student_id = a.student_id
            ORDER BY a.attendance_date DESC, s.name
        """).fetchall()

        if not rows:
            print("No attendance records found.")
            return

        print("-" * 80)
        print(f"{'ATT. ID':<10}{'STUDENT ID':<13}{'NAME':<25}{'DATE':<17}{'STATUS':<12}")
        print("-" * 80)
        for row in rows:
            print(f"{row[0]:<10}{row[1]:<13}{row[2][:23]:<25}{row[3]:<17}{row[4]:<12}")
        print("-" * 80)

    def show_attendance_chart(self):
        """Show a pie chart of all saved attendance records."""
        rows = self.conn.execute("""
            SELECT status, COUNT(*)
            FROM attendance
            GROUP BY status
        """).fetchall()

        counts = {"Present": 0, "Absent": 0}
        for status, total in rows:
            counts[status] = total

        labels = [status for status in ("Present", "Absent") if counts[status] > 0]
        values = [counts[label] for label in labels]

        if not values:
            print("No attendance data available. Mark attendance first.")
            return

        print("\nAttendance Summary")
        print(f"Present: {counts['Present']}")
        print(f"Absent : {counts['Absent']}")
        print(f"Total  : {sum(counts.values())}")

        plt.figure(figsize=(7, 5))
        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            explode=[0.04] * len(values)
        )
        plt.title("Student Attendance Summary")
        plt.axis("equal")
        plt.tight_layout()
        plt.show()

    # -------------------- MAIN MENU --------------------

    def run(self):
        while True:
            print("\n" + "=" * 48)
            print("       STUDENT MANAGEMENT SYSTEM")
            print("=" * 48)
            print("1. Add Student")
            print("2. View All Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Mark Attendance")
            print("6. View Attendance Records")
            print("7. Attendance Pie Chart")
            print("8. Exit")
            print("-" * 48)

            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.mark_attendance()
            elif choice == "6":
                self.view_attendance()
            elif choice == "7":
                self.show_attendance_chart()
            elif choice == "8":
                print("Thank you for using Student Management System.")
                break
            else:
                print("Invalid choice. Please select 1 to 8.")

    def close(self):
        """Close the SQLite connection."""
        self.conn.close()


if __name__ == "__main__":
    app = StudentManagementSystem()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nApplication stopped.")
    finally:
        app.close()
