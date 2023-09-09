import os
import csv

class Bank_Project:

    def __init__(self, data_folder):
        self.data_folder = data_folder

    def count_records_in_file(self, file_path):
        with open(file_path, 'r') as file:
            return sum(1 for line in file)

    def find_max_min_balance(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            max_balance = -float('inf')
            min_balance = float('inf')  
            problematic_lines = []
            for line_number, line in enumerate(lines[1:], start=2):
                parts = line.strip().split(',')
                if len(parts) == 5:
                    _,_ , _, balance,_ = parts
                    try:
                        balance = float(balance)
                        max_balance = max(max_balance, balance)
                        min_balance = min(min_balance, balance)
                    except ValueError:
                        problematic_lines.append((line_number, line.strip()))
            return max_balance, min_balance, problematic_lines

    def analyze_data(self):
        file_list = os.listdir(self.data_folder)
        total_files = len(file_list)
        for filename in file_list:
            if filename.endswith('.csv'):
                total_records = self.count_records_in_file(os.path.join(self.data_folder, filename))
                print(f"File: {filename}, Total Records: {total_records}")
                
                max_balance, min_balance, problematic_lines = self.find_max_min_balance(os.path.join(self.data_folder, filename))
                print(f"File: {filename}, Max Balance: {max_balance}, Min Balance: {min_balance}")
                
                if problematic_lines:
                    print(f"Problematic Lines in {filename}:")
                    for line_number, line in problematic_lines:
                        print(f"Line {line_number}: {line}")
                        
        overall_max_balance = -float('inf')
        overall_min_balance = float('inf')
        
        for filename in file_list:
            if filename.endswith('.csv'):
                max_balance, min_balance, _ = self.find_max_min_balance(os.path.join(self.data_folder, filename))
                overall_max_balance = max(overall_max_balance, max_balance)
                overall_min_balance = min(overall_min_balance, min_balance)
                
        print(f"Overall Max Balance: {overall_max_balance}, Overall Min Balance: {overall_min_balance}")
        
        total_savings = 0
        total_checking = 0
        
        for filename in file_list:
            if filename.endswith('.csv'):
                with open(os.path.join(self.data_folder, filename), 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        acc_type = line.strip().split(',')
                        if acc_type[4] == 'savings':
                            total_savings += 1
                        elif acc_type[4] == 'checking':
                            total_checking += 1
                            
        print(f"Total Savings Accounts: {total_savings}, Total Checking Accounts: {total_checking}")
        
        total = 0
        for filename in file_list:
            if filename.endswith(".csv"):
                with open(os.path.join(self.data_folder, filename), "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        acc_info = line.strip().split(",")
                        total += int(acc_info[3])
                        
        print(f"Total Bank Amount: {total}")
