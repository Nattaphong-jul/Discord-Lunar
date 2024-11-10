import os
import csv

def ensure_data_directories():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Stored in: {script_dir}")
    # Define the paths
    data_dir = script_dir + "Data"
    temp_data_dir = script_dir + "temp/Data"

    # Check and create /Data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
        print(f"Directory '{data_dir}' created.")
    else:
        print(f"Directory '{data_dir}' already exists.")

    # Check and create temp/Data directory if it doesn't exist
    if not os.path.exists(temp_data_dir):
        os.makedirs(temp_data_dir, exist_ok=True)
        print(f"Directory '{temp_data_dir}' created.")
    else:
        print(f"Directory '{temp_data_dir}' already exists.")

def check_or_create_log():
    # Define the filename
    filename = "log.csv"
    # Check if the file exists
    if not os.path.isfile(filename):
        # Define the headers
        headers = ["Date", "Time", "Server", "Channel", "UserID", "Sender", "Message"]
        
        # Create the file and write the header
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        
        print(f"{filename} created with headers.")
    else:
        print(f"{filename} already exists.")

ensure_data_directories()
check_or_create_log()