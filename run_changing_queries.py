import os
import sqlite3

folder_path = '\HW'

conn = sqlite3.connect(f'{folder_path}\Home_work.db')
cursor = conn.cursor()

query_files = {
    '1': 'query-1.sql',
    '2': 'query-2 copy.sql',
    '3': 'query-3 copy.sql',
    '4': 'query-4 copy.sql',
    '5': 'query-5 copy.sql',
    '6': 'query-6 copy.sql',    
    '7': 'query-7 copy.sql',
    '8': 'query-8 copy.sql',
    '9': 'query-9 copy.sql',  
    '10': 'query-10 copy.sql'
}

print("Available SQL queries:")
for option, query_name in query_files.items():
    print(f"{option}. {query_name}")

user_input = input("Enter the number of the query you want to execute (or 'exit' to exit): ")

while user_input.lower() != "exit":
    if user_input in query_files:
        selected_query = query_files[user_input]
        file_path = os.path.join(folder_path, selected_query)

        # Read the SQL query from the file
        with open(file_path, 'r') as file:
            query = file.read()

        # Prompt the user for additional parameters
        student_id = input("Enter student_id (mandatory for use in queries 9,10): ")
        subject_id = input("Enter subject_id (mandatory for use in queries 2,3,7): ")
        teacher_id = input("Enter teacher_id (mandatory for use in queries 5,8,10): ")
        group_id = input("Enter group_id (mandatory for use in queries 6,7): ")
        
        # Replace placeholders in the query with the user-provided parameters
        query = query.replace("<student_id>", student_id)
        query = query.replace("<subject_id>", subject_id)
        query = query.replace("<teacher_id>", teacher_id)
        query = query.replace("<group_id>", group_id)

        print(f"\nExecuting {selected_query}:")
        # print(query)

        # Execute the SQL query
        try:
            cursor.execute(query)
                    # Optionally, fetch the results
            results = cursor.fetchall()
            for row in results:
                print(row)
        except sqlite3.OperationalError:
            print("Invalid id. Please enter correct id.")


    else:
        print("Invalid input. Please enter a valid number or 'exit' to exit.")

    user_input = input("Enter the number of the query you want to execute (or 'exit' to exit): ")

conn.close()
