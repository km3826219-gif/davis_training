with open("student.txt", "r") as file:

    students = []
    topper = None
    highest_percentage = 0

    for line in file:
        try:
            if line.lower().startswith("id"):
                continue

            if line.strip() == "":
                continue

            data = [x.strip() for x in line.strip().split(",")]

            if len(data) != 6:
                raise ValueError("Wrong number of columns")

            sid, name, cls = data[0], data[1], data[2]

            m1 = int(data[3]) if data[3] else 0
            m2 = int(data[4]) if data[4] else 0
            m3 = int(data[5]) if data[5] else 0

            total = m1 + m2 + m3
            percentage = total / 3

            if percentage >= 90:
                grade = "A"
            elif percentage >= 75:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            else:
                grade = "Fail"

            students.append((name, cls, percentage, grade))

            if percentage > highest_percentage:
                highest_percentage = percentage
                topper = name

        except Exception as e:
            print("Invalid data:", line.strip(), "| Error:", e)

print("\nStudent Results:")
for s in students:
    print("Name:", s[0], "| Class:", s[1], "| %:", s[2], "| Grade:", s[3])

print("\nTopper:", topper, "| Percentage:", highest_percentage)