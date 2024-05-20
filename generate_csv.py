import csv

data = [
    ['Name', 'Country'],
    ['Mustapha', 'Algeria'],
    ['Said', 'Morocco'],
    ['Chris', 'U.S.A']
]

csv_file_path = 'countries_inventory.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' generated successfully.")
