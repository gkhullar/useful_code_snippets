#Script to record click events on plots of astronomy images
#AUTHOR: Gourav Khullar (using Astropy and Matplotlib)

#Usage format on command line
#python click_event.py image_fits_filename 
#(use filename argument if supplying own file)

import matplotlib.pyplot as plt
import numpy as np
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
import sys

SUPPLIED_OWN_FILE = False

if SUPPLIED_OWN_FILE:
    fits_image_filename = sys.argv[1]
    hdul = fits.open(fits_image_filename)
    #fits.info(hdu1)
    image_data = hdul[1].data
    #image_data = fits.getdata(hdu1, ext=0)
    hdul.close()
else:
    image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
    image_data = fits.getdata(image_file, ext=0)


event_array = []
def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'
        %(event.button, event.x, event.y, event.xdata, event.ydata))
    event_array.append([event.xdata, event.ydata])


fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(image_data, cmap='gray')
#ax.plot(np.random.rand(10))
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()


fig.canvas.mpl_disconnect(cid)
event_array=np.array(event_array)
#print(event_array)
np.savetxt('./save_data_of_clicks.txt',event_array)
