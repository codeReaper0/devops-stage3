def log_message(message):
    from datetime import datetime
    with open('/var/log/messaging_system.log', 'a') as f:
        # Format timestamp for readability
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}: {message}\n")
