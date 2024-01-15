import os
import sqlite3

folder_path = '\HW'

conn = sqlite3.connect(f'{folder_path}\Home_work.db')
cursor = conn.cursor()

query_files = {
    '1': 'query-1.sql',
    '2': 'query-2.sql',
    '3': 'query-3.sql',
    '4': 'query-4.sql',
    '5': 'query-5.sql',
    '6': 'query-6.sql',    
    '7': 'query-7.sql',
    '8': 'query-8.sql',
    '9': 'query-9.sql',  
    '10': 'query-10.sql'
}

print("Available SQL queries:")
for option, query_name in query_files.items():
    print(f"{option}. {query_name}")

user_input = input("Enter the number of the query you want to execute (or 'exit' to exit): ")

while user_input.lower() != "exit":
    if user_input in query_files:
        selected_query = query_files[user_input]
        file_path = os.path.join(folder_path, selected_query)
        
        with open(file_path, 'r') as file:
            query = file.read()

        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    else:
        print("Invalid input. Please enter a valid number or 'exit' to exit.")

    user_input = input("Enter the number of the query you want to execute (or 'exit' to exit): ")

conn.close()
