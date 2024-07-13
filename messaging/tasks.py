import os
from datetime import datetime


def log_message(message):
    # Get the current working directory
    current_dir = os.getcwd()

    # Construct the absolute path to the parent directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Construct the log directory path
    log_dir = os.path.join(parent_dir, 'devops-stage3', 'var', 'log')
    log_file = os.path.join(log_dir, "messaging_system.log")

    try:
        os.makedirs(log_dir, exist_ok=True)

        with open(log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}: {message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")
