import csv
import random

# Number of stars to generate
n = 10000  # You can change this value

# Function to generate random RA and DEC values
def generate_random_coordinates(n):
    data = []
    for i in range(1, n + 1):
        ra = random.uniform(0, 360)  # RA in range [0, 360) degrees
        dec = random.uniform(-90, 90)  # DEC in range [-90, 90] degrees
        data.append([i, ra, dec])
    return data

# Generate data
stars_data = generate_random_coordinates(n)

# Write data to a CSV file
csv_filename = "RANDOM_Stars.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Star Number", "RA (Decimal Degrees)", "DEC (Decimal Degrees)"])  # Header
    writer.writerows(stars_data)

print(f"CSV file '{csv_filename}' created with {n} stars.")
