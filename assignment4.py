import csv
with open("attendance.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Date","Status"])
    
    writer.writerow(["Arun","1-10-2026","Present"])
    writer.writerow(["Arun","2-10-2026","Present"])
    writer.writerow(["Arun","3-10-2026","Absent"])
    writer.writerow(["Arun","4-10-2026","Present"])
    writer.writerow(["Arun","5-10-2026","Present"])
    writer.writerow(["Anu","1-10-2026","Present"])
    writer.writerow(["Anu","2-10-2026","Present"])
    writer.writerow(["Anu","3-10-2026","Present"])
    writer.writerow(["Anu","4-10-2026","Absent"])
    writer.writerow(["Anu","5-10-2026","Present"])
    writer.writerow(["Akhil","1-10-2026","Present"])
    writer.writerow(["Akhil","2-10-2026","Present"])
    writer.writerow(["Akhil","3-10-2026","Present"])
    writer.writerow(["Akhil","4-10-2026","Present"])
    writer.writerow(["Akhil","5-10-2026","Present"])


attendance={}

with open("attendance.csv","r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        name=row["Name"]
        status=row["Status"]
        if status not in ["Present","Absent"]:
            print("Invalid record:",row)
            continue
        if name not in attendance:
            attendance[name]={"Present":0,"Absent":0}
        attendance[name][status]+=1
with open("attendance_report.txt","w") as file:
    for name,data in attendance.items():
        present=data["Present"]
        absent=data["Absent"]
        percentage=present/(present+absent)*100
        report=(
            f"Employee:{name}\n"
            f"Present:{present}\n"
            f"Absent:{absent}\n"
            f"Attendance:{percentage:.2f}%\n"
        )
        if percentage<75:
            report+="Attendance below 75%\n"
        print(report)
        file.write(report+"\n")
print("Report created successfully!")
while True:
    n=int(input("Enter option\n1.For adding new attendance\n2.Exit:  "))
    if n==1:
        name=input("Enter employee name: ")
        date=input("Enter date: ")
        status=input("Enter status(Present/Absent): ").capitalize()

        if name.strip() and date.strip and status in ["Present","Absent"]:
            with open("attendance.csv","a",newline="") as file:
                writer=csv.writer(file)
                writer.writerow([name,date,status])
            print("Attendance added successfully!")
        else:
            print("Invalid input!")
    if n==2:
        break








