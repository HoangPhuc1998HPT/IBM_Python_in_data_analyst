from datetime import datetime
import pandas as pd

# Define start and end dates for the plan
start_date = datetime(2025, 1, 23)
end_date = datetime(2025, 2, 28)

# Generate a list of dates for the plan
date_range = pd.date_range(start=start_date, end=end_date)

# Define content template
content = {
    "Listening": [
        "Listening Section 1 & 2", "Listening Section 3 & 4",
        "Review Listening mistakes", "Mock Listening Test"
    ],
    "Reading": [
        "Reading Passage 1", "Reading Passage 2",
        "Reading Passage 3", "Mock Reading Test"
    ],
    "Writing": [
        "Writing Task 1 (chart/graph)", "Writing Task 2 (essay)",
        "Review Writing Task 1", "Review Writing Task 2"
    ],
    "Speaking": [
        "Speaking Part 1 Practice", "Speaking Part 2 (Cue Card)",
        "Speaking Part 3 Discussion", "Mock Speaking Test"
    ],
    "Vocabulary & Grammar": [
        "Vocabulary Review (Morning session)",
        "Grammar Practice (Afternoon session)"
    ]
}

# Prepare the daily plan data
daily_plan = []
week_number = 1

for i, current_date in enumerate(date_range):
    if i % 7 == 0 and i > 0:  # Increment the week number after every 7 days
        week_number += 1

    # Create the daily schedule
    schedule = (
        f"7:00-9:00: {content['Listening'][i % len(content['Listening'])]}, "
        f"13:00-14:30: {content['Reading'][i % len(content['Reading'])]}"
    )

    # Split schedule into morning and afternoon components
    parts = schedule.split(", ")
    morning_part = parts[0]
    afternoon_part = parts[1]

    # Further split into time and content
    morning_time, morning_content = morning_part.split(": ", 1)
    afternoon_time, afternoon_content = afternoon_part.split(": ", 1)

    # Append structured data to the plan
    plan = {
        "Week Number": f"Week {week_number}",
        "Day": f"Day {i % 7 + 1}",
        "Date": current_date.strftime("%Y-%m-%d"),
        "Morning Time": morning_time,
        "Morning Content": morning_content,
        "Afternoon Time": afternoon_time,
        "Afternoon Content": afternoon_content,
        "Goal": "Focus on improving skills systematically based on the IELTS test sections.",
        "Result (To Fill)": ""
    }
    daily_plan.append(plan)

# Convert the plan into a DataFrame
df_monthly_plan = pd.DataFrame(daily_plan)

# Save to Excel
file_path_monthly = "H:/My Drive/Monthly_Study_Plan_Detailed.xlsx"  # Change this path as needed
df_monthly_plan.to_excel(file_path_monthly, index=False, sheet_name="Study Plan", engine="openpyxl")

print(f"File đã được xuất thành công tại: {file_path_monthly}")
