import os
import csv


data_folder = '/Users/Sliem/Desktop/data/'


# Task 1:
def count_records_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_list = os.listdir(data_folder)
total_files = len(file_list)

for filename in file_list:
    if filename.endswith('.csv'):
        total_records = count_records_in_file(os.path.join(data_folder, filename))
        print(f"File: {filename}, Total Records: {total_records}")

# Task 2: 
def find_max_min_balance(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        max_balance = -float('inf')
        min_balance = float('inf')
        problematic_lines = []  #
        for line_number, line in enumerate(lines[1:], start=2): 
            parts = line.strip().split(',')
            if len(parts) == 5:
                _, _, _, balance, _ = parts
                try:
                    balance = float(balance)
                    max_balance = max(max_balance, balance)
                    min_balance = min(min_balance, balance)
                except ValueError:
                    problematic_lines.append((line_number, line.strip()))
        return max_balance, min_balance, problematic_lines

for filename in file_list:
    if filename.endswith('.csv'):
        max_balance, min_balance, problematic_lines = find_max_min_balance(os.path.join(data_folder, filename))
        print(f"File: {filename}, Max Balance: {max_balance}, Min Balance: {min_balance}")
        if problematic_lines:
            print(f"Problematic Lines in {filename}:")
            for line_number, line in problematic_lines:
                print(f"Line {line_number}: {line}")

# Task 3: 
overall_max_balance = -float('inf')
overall_min_balance = float('inf')

for filename in file_list:
    if filename.endswith('.csv'):
        max_balance, min_balance, _ = find_max_min_balance(os.path.join(data_folder, filename))
        overall_max_balance = max(overall_max_balance, max_balance)
        overall_min_balance = min(overall_min_balance, min_balance)

#NEW PART
maxb = -1
minb = -1
l_name = ""
f_name = ""
listmax = [1]
listmin = [1]
for filename in file_list:
    if filename.endswith(".csv"):
        with open(os.path.join(data_folder, filename), "r") as file:
            lines = file.readlines()
            for line in lines:
                info = line.strip().split(",")
                print(info)
                nums = int(info[3])
                if nums > maxb:
                    maxb = nums
                    f_name = info[1]
                    l_name = info[2]
print(f_name)
print(l_name)
#NEW PART ENDS

print(f"Overall Max Balance: {overall_max_balance}, Overall Min Balance: {overall_min_balance}")

# Task 4: 
total_savings = 0
total_checking = 0

for filename in file_list:
    if filename.endswith('.csv'):
        with open(os.path.join(data_folder, filename), 'r') as file:
            lines = file.readlines()
            for line in lines:
                acc_type = line.strip().split(',')
                if acc_type[4] == 'savings':
                    total_savings += 1
                elif acc_type[4] == 'checking':
                    total_checking += 1

print(f"Total Savings Accounts: {total_savings}, Total Checking Accounts: {total_checking}")

# Task 5
total = 0

for filename in file_list:
    if filename.endswith(".csv"):
        with open(os.path.join(data_folder, filename), "r") as file:
            lines = file.readlines()
            for line in lines:
                acc_info = line.strip().split(",")
                total += int(acc_info[3])
print(f"Total Bank Amount: {total}")
