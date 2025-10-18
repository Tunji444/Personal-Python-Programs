import time
import winsound

def set_alarm(hour: int, minute: int):
    
    # Validating the hour and minute values
    if hour < 0 or hour > 23:
        raise ValueError("Invalid hour value. Please enter a value between 0 and 23.")
    if minute < 0 or minute > 59:
        raise ValueError("Invalid minute value. Please enter a value between 0 and 59.")

    # Getting the current time
    current_time = time.localtime()

    # Calculating the remaining time until the alarm goes off
    remaining_hours = hour - current_time.tm_hour
    remaining_minutes = minute - current_time.tm_min

    # Converting negative remaining minutes to hours
    if remaining_minutes < 0:
        remaining_hours -= 1
        remaining_minutes += 60

    # Converting negative remaining hours to next day
    if remaining_hours < 0:
        remaining_hours += 24

    # Calculating the total remaining seconds
    remaining_seconds = remaining_hours * 3600 + remaining_minutes * 60

    # Sleeping until the alarm time
    time.sleep(remaining_seconds)

    # Playing the alarm sound
    winsound.Beep(1000, 2000)  # Beep at 1000 Hz for 2 seconds

# Example usage of the set_alarm function
try:
    alarm_hour = int(input("Enter the hour for the alarm (0-23): "))
    alarm_minute = int(input("Enter the minute for the alarm (0-59): "))
    set_alarm(alarm_hour, alarm_minute)
    print("Alarm has gone off!")
except ValueError as e:
    print(f"Error: {e}")