import csv
import pandas as pd
import json
import pickle
import sqlite3

def import_txt_file(file_path):
    """
    Import data from a text file.

    Parameters:
    - file_path (str): Path to the text file.

    Returns:
    - str: Content of the text file.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def import_csv_file(file_path):
    """
    Import data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - list: List of lists containing CSV data.
    """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def import_excel_file(file_path, sheet_name='Sheet000', header=0, usecols=None):
    """
    Import data from an Excel file.

    Parameters:
    - file_path (str): Path to the Excel file.
    - sheet_name (str): Name of the Excel sheet. Default is 'Sheet1'.
    - header (int): Row number to use as header. Default is 0.
    - usecols (list): List of columns to select. Default is None.

    Returns:
    - pandas.DataFrame: DataFrame containing the Excel data.
    """
    data = pd.read_excel(file_path, sheet_name=sheet_name, header=header, usecols=usecols)
    return data

def import_pickle_file(file_path):
    """
    Import data from a pickle file.

    Parameters:
    - file_path (str): Path to the pickle file.

    Returns:
    - any: Content of the pickle file.
    """
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def import_json_file(file_path):
    """
    Import data from a JSON file.

    Parameters:
    - file_path (str): Path to the JSON file.

    Returns:
    - dict: Dictionary containing JSON data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def import_html_file(file_path):
    """
    Import data from an HTML file.

    Parameters:
    - file_path (str): Path to the HTML file.

    Returns:
    - str: Text content of the HTML file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def import_sqlite_database(file_path, query):
    """
    Import data from a SQLite database.

    Parameters:
    - file_path (str): Path to the SQLite database file.
    - query (str): SQL query to execute.

    Returns:
    - list: List of tuples containing query results.
    """
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == '__main__':

    txt_data = import_txt_file('/Users/hritvikmahajan/Downloads/ALY6140/data/network_data.txt')
    csv_data = import_csv_file('/Users/hritvikmahajan/Downloads/ALY6140/data/Neural_data.csv')
    excel_data = import_excel_file('/Users/hritvikmahajan/Downloads/ALY6140/data/Excel_report.xlsx')
    pickle_data = import_pickle_file('/Users/hritvikmahajan/Downloads/ALY6140/data/iris_data.pkl')
    json_data = import_json_file('/Users/hritvikmahajan/Downloads/ALY6140/data/nested_data.json')
    html_data = import_html_file('/Users/hritvikmahajan/Downloads/ALY6140/data/grativational_wave.html')
    sqlite_data = import_sqlite_database('/Users/hritvikmahajan/Downloads/ALY6140/data/chinook.db', 'SELECT * FROM invoices')


    print(txt_data)
    print(csv_data)
    print(excel_data)
    print(pickle_data)
    print(json_data)
    print(html_data)
    print(sqlite_data)
