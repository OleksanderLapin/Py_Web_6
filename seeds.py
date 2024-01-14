from faker import Faker
from random import randint
import sqlite3 


conn = sqlite3.connect('Home_work.db')
cursor = conn.cursor()

fake = Faker()
NUM_TEACHERS = 5
NUM_STUDENTS = 50
NUM_GRADES = 20
groups = ['Group 1', 'Group 2', 'Group 3']
subjects = ['Mathematics', 'Science', 'History', 'English', 'Computer Science']
grades_num = int(NUM_GRADES/len(subjects))

def seed_teachers():
    teachers = [fake.name() for _ in range(NUM_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(?);"
    cursor.executemany(sql, zip(teachers,))

def seed_groups():
    sql = "INSERT INTO groups(name) VALUES(?);"
    cursor.executemany(sql, zip(groups,))

def seed_subjects():
    sql = "INSERT INTO subjects(name, teacher_id) VALUES(?, ?);"
    cursor.executemany(sql, zip(subjects, iter(randint(1,NUM_TEACHERS) for _ in range(len(subjects)))))

def seed_students():
    students = [fake.name() for _ in range(NUM_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    cursor.executemany(sql, zip(students, iter(randint(1,len(groups)) for _ in range(len(students)))))

def seed_grades():
    sql = "INSERT INTO grades (student_id, subject_id, grade, date_taken) VALUES (?, ?, ?, ?)"
    for student_id in range(1, NUM_STUDENTS+1):
        for subject_id in range(1, len(subjects)+1):
            for _ in range(randint(1,grades_num)):
                date_taken = fake.date_between(start_date='-200d', end_date='-100d')
                grade = randint(1, 100)
                cursor.execute(sql, (student_id, subject_id, grade, date_taken))
            

if __name__ == "__main__":
    try:
        seed_teachers()
        seed_subjects()
        seed_groups()
        seed_students()
        seed_grades()
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
