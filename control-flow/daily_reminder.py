# daily_reminder.py

# Prompt user for input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Validate task input
if not task:
    print("Task description cannot be empty.")
    exit(1)

# Generate base message based on priority
if priority == "high":
    message = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    message = f"Note: '{task}' is a medium priority task"
elif priority == "low":
    message = f"Note: '{task}' is a low priority task"
else:
    message = f"Note: '{task}' has an unspecified priority level"

# Append time-sensitive message
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Display the final reminder
print(message)

