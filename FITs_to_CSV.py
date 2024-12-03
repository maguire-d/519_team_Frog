import csv
from astropy.io import fits

# Open the FITS file and extract data
with fits.open("DESY_LT_crossmatch.fits") as hdul:
    data = hdul[1].data

    # Replace 'RA' and 'DEC' with the actual column names in your data
    ra = data['RA']  
    dec = data['DEC']  

    # Write to a CSV file
    with open('stars.csv', mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write the header row
        csvwriter.writerow(['Star Number', 'RA', 'Dec'])
        
        # Write data rows
        for i in range(len(ra)):
            csvwriter.writerow([i + 1, ra[i], dec[i]])

print("CSV file 'stars.csv' created successfully.")
