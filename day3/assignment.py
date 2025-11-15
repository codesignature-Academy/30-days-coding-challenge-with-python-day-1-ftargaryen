user_score = int(input("enter your score: "))
user_dept = input("enter your department: ")

if user_dept == "medicine":
    cutoff = 250
elif user_dept == "engineering":
    cutoff = 220
elif user_dept == "law":
    cutoff = 240
elif user_dept == "business":
    cutoff = 180

else:
    print("invalid department")

if user_score>= cutoff:
    print(f"congratulations you're admitted into the department of {user_dept}")

else:
    print("sorry you were not admitted")