import numpy as np
import scipy as sp
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from astropy.wcs import WCS
import pandas as pd

gaia_coord = 
dwarf_coord = 

gaia_data = pd.DataFrame({
    'RA': gaia_coord[0],
    'DEC': gaia_coord[1],
    'Index': range(len(gaia_coord[0]))
})

dwarf_data = pd.DataFrame({
    'RA': dwarf_coord[0],
    'DEC': dwarf_coord[1],
    'Index': range(len(dwarf_coord[0]))
})

########## Seems like we may not use this file but Ill keep it for now