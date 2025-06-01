task = input("Enter your task: ") 
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
elif priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that should be done today.")
    else:
        print(f"Note: '{task}' is a medium priority task. Plan to work on it soon.")
elif priority == "low":
    if time_bound == "yes":
        print(f"Note: '{task}' is a low priority task but is time-bound. Try to finish it soon.")
    else:
        print(f"Note: '{task}' is a low priority task. Work on it when possible.")
else:
    print("Invalid priority entered. Please enter high, medium, or low.")
