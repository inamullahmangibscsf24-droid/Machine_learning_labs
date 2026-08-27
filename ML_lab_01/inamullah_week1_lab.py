# Inamullah - bscs - 5 - sec- G  023-24-0236

# Q1
a = 10
b = 20
print(f"a={a}, b={b}")
a = a + b
b = a - b
a = a - b
print(f"Swapped: a={a}, b={b}\n")

# Q2
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print("Prime numbers in [2,7,10,17,29]:")
for x in [2, 7, 10, 17, 29]:
    print(f"  {x}: {is_prime(x)}\n")

# Q3
n = 10
a, b = 0, 1
fib = []
i = 0
while i < n:
    fib.append(a)
    temp = a + b
    a = b
    b = temp
    i += 1
print(f"Fibonacci({n} terms): {fib}\n")

# Q4
def remove_dups(lst):
    result = []
    i = 0
    while i < len(lst):
        found = False
        j = 0
        while j < len(result):
            if result[j] == lst[i]:
                found = True
                break
            j += 1
        if not found:
            result.append(lst[i])
        i += 1
    return result

lst = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(f"Original: {lst}")
print(f"  Unique: {remove_dups(lst)}\n")

# Q5
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(f"multiply(2,3,4) = {multiply(2, 3, 4)}")
print(f"  multiply(5,2,3,4) = {multiply(5, 2, 3, 4)}\n")

# Q6
text = "hello world"
char_freq = {}
i = 0
while i < len(text):
    ch = text[i]
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1
    i += 1
print(f"'{text}' -> {char_freq}\n")

# Q7
employees = [
    {'name': 'Alice', 'salary': 50000},
    {'name': 'Bob', 'salary': 75000},
    {'name': 'Diana', 'salary': 85000},
    {'name': 'Frank', 'salary': 70000}
]
max_emp = employees[0]
i = 1
while i < len(employees):
    if employees[i]['salary'] > max_emp['salary']:
        max_emp = employees[i]
    i += 1
print(f"Highest paid: {max_emp['name']} (${max_emp['salary']})\n")

# Q8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
odd = []
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        odd.append(numbers[i])
    i += 1
print(f"Odd from {numbers}")
print(f"  -> {odd}\n")

# Q9
import numpy as np
arr = []
i = 1
while i <= 30:
    arr.append(i)
    i += 1
matrix = []
for i in range(5):
    row = []
    for j in range(6):
        row.append(arr[i * 6 + j])
    matrix.append(row)
result = np.array(matrix)
print(f"Reshape 1-30 to 5x6:\n{result}\n")

# Q10
matrix = []
i = 0
while i < 6:
    row = []
    j = 0
    while j < 6:
        if i == j:
            row.append(i + 1)
        else:
            row.append(0)
        j += 1
    matrix.append(row)
print(f"Identity with diagonal [1,2,3,4,5,6]:\n{np.array(matrix)}\n")

# Q11
arr = [45, 23, 67, 89, 12, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 21, 32, 43, 54, 65, 76]
total = 0
i = 0
while i < len(arr):
    total += arr[i]
    i += 1
mean = total / len(arr)
sq_diff = 0
i = 0
while i < len(arr):
    sq_diff += (arr[i] - mean) ** 2
    i += 1
std_dev = (sq_diff / len(arr)) ** 0.5
print(f"Sum={total}, Mean={mean:.2f}, StdDev={std_dev:.2f}\n")

# Q12
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
diag_sum = 0
i = 0
while i < len(matrix):
    diag_sum += matrix[i][i]
    i += 1
print(f"4x4 diagonal sum: {diag_sum}\n")

# Q13
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
elem_wise = []
i = 0
while i < 3:
    row = []
    j = 0
    while j < 3:
        row.append(A[i][j] * B[i][j])
        j += 1
    elem_wise.append(row)
print(f"Element-wise multiplication:\n{np.array(elem_wise)}\n")

# Q14
temps = [22, 35, 38, 30, 40, 32, 36, 28, 37, 39, 25, 41, 33, 29, 42, 31, 34, 26, 43, 27, 44, 24, 35, 37, 23, 38, 30, 40, 32, 36]
count = 0
i = 0
while i < len(temps):
    if temps[i] > 35:
        count += 1
    i += 1
print(f"Days with temp > 35°C: {count} out of {len(temps)}\n")

# Q15
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
min_val = arr[0]
max_val = arr[0]
i = 0
while i < len(arr):
    if arr[i] < min_val:
        min_val = arr[i]
    if arr[i] > max_val:
        max_val = arr[i]
    i += 1
normalized = []
i = 0
while i < len(arr):
    norm = (arr[i] - min_val) / (max_val - min_val)
    normalized.append(norm)
    i += 1
print(f"Original: {arr}")
print(f"  Normalized: {[round(x, 2) for x in normalized]}\n")

# Q16
marks = [[85, 90, 88], [78, 82, 80], [92, 88, 91], [88, 85, 87], [75, 79, 81]]
print("Per-student totals and averages:")
i = 0
while i < len(marks):
    total = 0
    j = 0
    while j < len(marks[i]):
        total += marks[i][j]
        j += 1
    avg = total / len(marks[i])
    print(f"  Student {i+1}: Total={total}, Avg={avg:.2f}")
    i += 1
print()

# Q17
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = []
i = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        result.append(-1)
    else:
        result.append(arr[i])
    i += 1
print(f"Replace even with -1: {result}\n")

# Q18
import pandas as pd
students = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'section': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'marks': [85, 78, 92, 88, 75, 89, 91, 82]
})
print(f"Student DataFrame:\n{students}\n")

# Q19
df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'Diana'],
    'age': [22, None, 20, 23],
    'marks': [85, 78, None, 88]
})
print(f"Missing values before:\n{df.isnull().sum()}")
df['age'].fillna(df['age'].mean(), inplace=True)
df['marks'].fillna(df['marks'].mean(), inplace=True)
print(f"After filling:\n{df}\n")

# Q20
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'marks': [85, 45, 30, 88, 42, 75]
})
low = df[df['marks'] < 50]
print(f"Students with marks < 50:\n{low[['name', 'marks']]}\n")

# Q21
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'section': ['A', 'B', 'A', 'B', 'A', 'B'],
    'marks': [85, 78, 92, 88, 75, 89]
})
print("GroupBy section stats:")
grouped = df.groupby('section')['marks'].agg(['mean', 'max'])
print(f"{grouped}\n")

# Q22
students_df = pd.DataFrame({'student_id': [1, 2, 3, 4], 'name': ['Alice', 'Bob', 'Charlie', 'Diana']})
attendance_df = pd.DataFrame({'student_id': [1, 2, 3, 4], 'attendance': [90, 70, 85, 60]})
merged = pd.merge(students_df, attendance_df, on='student_id')
low_att = merged[merged['attendance'] < 75]
print(f"Students with attendance < 75%:\n{low_att[['name', 'attendance']]}\n")

# Q23
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'section': ['A', 'B'],
    'avg_marks': [84, 83.5]
})
plt.figure(figsize=(8, 5))
plt.bar(df['section'], df['avg_marks'], color=['red', 'blue'])
plt.xlabel('Section')
plt.ylabel('Average Marks')
plt.title('Average Marks per Section')
plt.show()

# Q24
marks = [85, 78, 92, 88, 75, 89, 91, 82, 79, 86, 90, 84, 77, 93, 88]
plt.figure(figsize=(10, 6))
plt.hist(marks, bins=8, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Student Marks')
plt.show()

# Q25
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
performance = [75, 78, 82, 85, 88, 92]
hours = [2, 3, 4, 5, 6, 7]
scores = [72, 75, 80, 85, 88, 91]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].plot(months, performance, marker='o', linewidth=2, color='red')
axes[0].set_title('Performance Trend')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Score')

axes[1].scatter(hours, scores, color='green', s=100)
axes[1].set_title('Study Hours vs Scores')
axes[1].set_xlabel('Hours')
axes[1].set_ylabel('Score')
plt.show()

