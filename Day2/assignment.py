print("⏰ Welcome to the Time Converter!")

minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutes(s) is equal to {hours} hour(s) and {remaining_minutes} minutes(s)")