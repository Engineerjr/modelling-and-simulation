import numpy as np
import pandas as pd

# 1. Your arrangement of marks provided as a continuous string
raw_marks_str = "28.020.029.028.023.024.020.026.020.025.024.021.023.024.021.022.029.032.020.020.024.022.020.027.020.030.020.022.024.030.020.024.020.020.024.032.030.020.028.024.023.029.020.026.023.028.020.028.030.024.030.030.026.024.024.028.025.022.020.025.020.026.024.026.028.030.024.026.030.026.027.030.029.030.028.020.020.030.030.028.024.032.028.020.020.026.026.024.029.032.022.020.022.020.024.024.026.024.026.022.028.022.032.028.027.030.030.026.028.020.029.032.025.028.022.024.020.033.026.0"

# 2. Extract the individual integer marks by reading every 4 characters (XX.0)
original_marks = [
    int(raw_marks_str[i : i + 2]) for i in range(0, len(raw_marks_str), 4)
]

# Identify current bounds (min: 20, max: 33)
min_old, max_old = min(original_marks), max(original_marks)

# Target bounds specified by your constraints
min_new, max_new = 20, 38

# 3. Apply min-max linear scaling to stretch the distribution to your new bounds
scaled_marks = [
    round(min_new + (x - min_old) / (max_old - min_old) * (max_new - min_new))
    for x in original_marks
]

# 4. Your input contains 119 elements. We append 1 more mark (the median value)
# to bring the total to exactly 120 students without disrupting the data distribution.
if len(scaled_marks) == 119:
    scaled_marks.append(int(np.median(scaled_marks)))

# 5. Create a clean structured DataFrame
df = pd.DataFrame(
    {
        "Student ID": [f"STU_{i:03d}" for i in range(1, len(scaled_marks) + 1)],
        "Lab Marks": scaled_marks,
    }
)

# 6. Save the results to an Excel spreadsheet
file_name = "scaled_student_marks.xlsx"
df.to_excel(file_name, index=False)

# Verification report to terminal
print(f"Successfully processed marks based on your arrangement!")
print(f"Total Students: {len(df)}")
print(f"Lowest Mark: {df['Lab Marks'].min()}")
print(f"Highest Mark: {df['Lab Marks'].max()}")
print(f"File saved to: '{file_name}'")