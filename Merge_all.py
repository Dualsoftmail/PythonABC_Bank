import csv

input_files = ['data1.csv', 'data2.csv', 'data3.csv']
output_file = 'account.txt'
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    for input_file in input_files:
        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)
            
            for row in reader:
                writer.writerow(row)

print(f'Merged data from {", ".join(input_files)} into {output_file}.')
