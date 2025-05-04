# Load the hyperspectral image
from spectral import envi
img = envi.open('AVIS data/bioscape_v02_34_11_rfl.hdr', 'AVIS data/bioscape_v02_34_11_rfl')
print(img.shape, img.bands.centers[0], img.bands.centers[-1])


# Display a quick RGB composite
import matplotlib.pyplot as plt
import numpy as np

rgb = img.read_band(100), img.read_band(50), img.read_band(30)
plt.imshow(np.dstack(rgb))
plt.title('False Colour Composite of Scene')
plt.axis('off')

# Defining the Table Mountain ROI
import rasterio
from rasterio.mask import mask
import fiona

with fiona.open('Table Mountain/Table Mountain National Park.shp', 'r') as shp:
    polygons = [feature['geometry'] for feature in shp]

with rasterio.open('AVIS data/bioscape_v02_34_11_rfl') as src:
    clipped, out_transform = mask(src, polygons, crop=True)
