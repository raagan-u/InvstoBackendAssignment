import mysql.connector
from mysql.connector import Error
import csv
from datetime import datetime

def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='simplepassword12',
            database='work'
        )
        print("MySQl Database connection successful")
    except Error as err:
        print(f"Error: {err} ")

    return connection

def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        return True
    except Error as err:
        return False

def csv_to_list(csv_file):
    if not csv_file:
        print("Please Provide A CSV File Name")
        return None, -1
    listt = []
    with open(csv_file, 'r') as fd:
        reader = csv.reader(fd)
        i = 0
        for row in reader:
            if i==0:
                i = i+1
                continue
            i = i + 1
            try:
                row_list = []
                row_list.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"))
                row_list.append(float(row[1]))
                row_list.append(float(row[2]))
                row_list.append(float(row[3]))
                row_list.append(float(row[4]))
                row_list.append(int(row[5]))
                if str(row[6]) == "":
                    continue
                row_list.append(str(row[6]))
            except ValueError as e:
                print("record skipped : " ,e)
                continue

            listt.append(row_list)
    return listt,i-1

def write_to_table(conn,listt, csv_length):
    if csv_length == -1:
        print("No records were found to be inserted")
        return
    count = 0
    for row in listt:
        if not row:
            continue
        query = f'INSERT INTO hindalco values("{row[0]}",{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},"{row[6]}")'
        if execute_query(conn,query) == 1:
            count = count + 1
        else:
            pass
    print(f"{count} of {csv_length} records inserted successfully")


if __name__ == "__main__":
    conn = create_server_connection()
    write_to_table(conn, *csv_to_list("hindalco.csv")) #propercsv
