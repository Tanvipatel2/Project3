import time
def set_reminder(seconds, message):
    print("Reminder set...")
    time.sleep(seconds)
    return f"Reminder: {message}"
