import os

def ensure_data_directories():
    # Define the paths
    data_dir = "Data"
    temp_data_dir = "temp/Data"

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

# Example usage
ensure_data_directories()