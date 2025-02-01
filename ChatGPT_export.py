import pandas as pd

# Dữ liệu lịch học được chỉnh sửa với các số trang chính xác
corrected_practices = [
    # Test 1
    ("Listening Section 1 (Page 1-2)", "Reading Passage 1 (Page 20-21)"),
    ("Writing Task 1 (Page 22)", "Reading Passage 2 (Page 23-25)"),
    ("Listening Section 2 (Page 3-4)", "Speaking Part 1 (Page 26-27)"),
    ("Listening Section 3 (Page 5-6)", "Reading Passage 3 (Page 28-29)"),
    ("Mock Listening Test (Page 7-8)", "Mock Reading Test (Page 30-31)"),
    ("Writing Task 2 (Page 32)", "Speaking Part 2 and 3 (Page 33-34)"),
    ("Review Listening Mistakes (Page 35)", "Review Reading Mistakes (Page 36)"),

    # Test 2
    ("Listening Section 1 (Page 37-38)", "Reading Passage 1 (Page 39-40)"),
    ("Writing Task 1 (Page 41)", "Reading Passage 2 (Page 42-43)"),
    ("Listening Section 2 (Page 44-45)", "Speaking Part 1 (Page 46-47)"),
    ("Listening Section 3 (Page 48-49)", "Reading Passage 3 (Page 50-51)"),
    ("Mock Listening Test (Page 52-53)", "Mock Reading Test (Page 54-55)"),
    ("Writing Task 2 (Page 56)", "Speaking Part 2 and 3 (Page 57-58)"),
    ("Review Listening Mistakes (Page 59)", "Review Reading Mistakes (Page 60)"),

    # Test 3
    ("Listening Section 1 (Page 61-62)", "Reading Passage 1 (Page 63-64)"),
    ("Writing Task 1 (Page 65)", "Reading Passage 2 (Page 66-67)"),
    ("Listening Section 2 (Page 68-69)", "Speaking Part 1 (Page 70-71)"),
    ("Listening Section 3 (Page 72-73)", "Reading Passage 3 (Page 74-75)"),
    ("Mock Listening Test (Page 76-77)", "Mock Reading Test (Page 78-79)"),
    ("Writing Task 2 (Page 80)", "Speaking Part 2 and 3 (Page 81-82)"),
    ("Review Listening Mistakes (Page 83)", "Review Reading Mistakes (Page 84)"),

    # Test 4
    ("Listening Section 1 (Page 85-86)", "Reading Passage 1 (Page 87-88)"),
    ("Writing Task 1 (Page 89)", "Reading Passage 2 (Page 90-91)"),
    ("Listening Section 2 (Page 92-93)", "Speaking Part 1 (Review All)")
]

# Tạo lịch học từ dữ liệu
corrected_schedule = {
    "Week Number": [],
    "Day": [],
    "Date": [],
    "Morning Time": [],
    "Morning Content": [],
    "Afternoon Time": [],
    "Afternoon Content": [],
    "Practice Reference": [],
    "Goal": []
}

# Ngày bắt đầu
start_date = pd.to_datetime("2025-01-23")
total_days = len(corrected_practices)

# Tạo dữ liệu lịch học
for day, (morning, afternoon) in enumerate(corrected_practices):
    date = start_date + pd.Timedelta(days=day)
    corrected_schedule["Week Number"].append(f"Week {(day // 7) + 1}")
    corrected_schedule["Day"].append(f"Day {(day % 7) + 1}")
    corrected_schedule["Date"].append(date.strftime("%Y-%m-%d"))
    corrected_schedule["Morning Time"].append("7:00-9:00")
    corrected_schedule["Morning Content"].append(morning)
    corrected_schedule["Afternoon Time"].append("13:00-14:30")
    corrected_schedule["Afternoon Content"].append(afternoon)
    corrected_schedule["Practice Reference"].append(
        f"{morning.split('(')[1].split(')')[0]}, {afternoon.split('(')[1].split(')')[0]}")
    corrected_schedule["Goal"].append("Complete tasks and review mistakes")

# Chuyển đổi sang DataFrame
corrected_schedule_df = pd.DataFrame(corrected_schedule)

# Lưu vào file CSV
output_file_path = "H:/My Drive/Monthly_Study_Plan_Detailed.csv"
corrected_schedule_df.to_csv(output_file_path, index=False, encoding="utf-8")

print(f"Lịch học đã được lưu vào file: {output_file_path}")




