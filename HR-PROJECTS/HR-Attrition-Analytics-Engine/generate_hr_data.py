import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

num_employees = 1200

# ---------------------------
# Generate Base Columns
# ---------------------------

EmployeeID = np.arange(1, num_employees + 1)

Age = np.random.randint(21, 60, num_employees)

Department = np.random.choice(
    ['Sales', 'HR', 'Tech', 'Operations', 'Finance'],
    num_employees
)

TenureMonths = np.random.randint(1, 60, num_employees)

ShiftType = np.random.choice(
    ['Day', 'Night', 'Rotational'],
    num_employees
)

PerformanceScore = np.random.randint(1, 6, num_employees)

SupervisorRating = np.random.randint(1, 6, num_employees)

OvertimeHours = np.random.randint(0, 40, num_employees)

# ---------------------------
# Salary Logic (Tenure-based)
# ---------------------------

Salary = (
    30000
    + (TenureMonths * 500)
    + np.random.normal(0, 3000, num_employees)
)

Salary = Salary.round(0)

# ---------------------------
# Attrition Risk Logic
# ---------------------------

risk = np.full(num_employees, 0.15)

risk += np.where(TenureMonths < 12, 0.25, 0)
risk += np.where(OvertimeHours > 25, 0.25, 0)
risk += np.where(PerformanceScore < 3, 0.20, 0)

risk = np.clip(risk, 0, 0.9)

random_values = np.random.rand(num_employees)

Exit = np.where(random_values < risk, 1, 0)

# ---------------------------
# Create DataFrame
# ---------------------------

df = pd.DataFrame({
    'EmployeeID': EmployeeID,
    'Age': Age,
    'Department': Department,
    'TenureMonths': TenureMonths,
    'Salary': Salary,
    'OvertimeHours': OvertimeHours,
    'PerformanceScore': PerformanceScore,
    'SupervisorRating': SupervisorRating,
    'ShiftType': ShiftType,
    'Exit': Exit
})

# ---------------------------
# Validation
# ---------------------------

print("Dataset Shape:", df.shape)
print("Turnover Rate:", round(df['Exit'].mean() * 100, 2), "%")

# Save CSV
df.to_csv("sample_hr_data.csv", index=False)

print("CSV file created successfully.")