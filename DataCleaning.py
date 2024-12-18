import csv
import pandas as pd

binaries = True
planetary_masses = True
m_dwarfs = False

df = pd.read_csv('pre_matched_csv/BrownDwarfs.csv')
df_filtered = df.dropna(subset=['SPEC']).sort_values(by='SPEC')

if binaries:
    df_filtered = df_filtered[df_filtered['M?'].isna()]
if planetary_masses:
    df_filtered = df_filtered[df_filtered['PM?'].isna()]

print(df_filtered)
df_m_dwarves = df_filtered[df_filtered['SPEC'].str.startswith('M')]
df_no_m_dwarves = df_filtered[~df_filtered['SPEC'].str.startswith('M')]


def ra_to_degrees(ra_str):
    # Split the RA string into hours, minutes, and seconds
    try:
        hours, minutes, seconds = map(float, ra_str.split())
    except:
        return
    
    # Convert to degrees
    degrees = (hours * 15) + (minutes / 60 * 15) + (seconds / 3600 * 15)
    return degrees

def dec_to_degrees(dec_str):
    # Check if the declination is positive or negative
    sign = -1 if dec_str[0] == '-' else 1
    
    # Remove the sign and split the string into degrees, minutes, and seconds
    dec_str = dec_str.lstrip('+-')  # Remove sign
    degrees, minutes, seconds = map(float, dec_str.split())

    # Convert to degrees
    degrees_in_degrees = degrees + (minutes / 60) + (seconds / 3600)
    
    # Apply the sign
    return sign * degrees_in_degrees


if m_dwarfs:
    df_m_dwarves['RA'] = df_m_dwarves['RA'].apply(ra_to_degrees)
    df_m_dwarves['DEC'] = df_m_dwarves['DEC'].apply(dec_to_degrees)

    df_m_dwarves.to_csv('JOHNSTON_MDwarfs.csv', index=False)

else:
    df_no_m_dwarves['RA'] = df_no_m_dwarves['RA'].apply(ra_to_degrees)
    df_no_m_dwarves['DEC'] = df_no_m_dwarves['DEC'].apply(dec_to_degrees)

    df_no_m_dwarves.to_csv('JOHNSTON_NotMDwarfs.csv', index=False)
