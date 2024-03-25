import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


#ładowanie pliku nii
nifti_file = nib.load('a1.nii')
nifti_data = nifti_file.get_fdata()

#skalowanie do koloru
data_scaled = nifti_data / np.max(nifti_data)
merged_image = np.stack((data_scaled[:, :,:, 0], data_scaled[:, :,:, 1], data_scaled[:, :,:, 2]), axis=-1)

#wybor warstwy

layer = 60
choose_layer = merged_image[:,layer,:,:]

# Funkcja do aktualizacji warstwy
def update_layer(change):
    global layer, choose_layer
    if change == 'next':
        layer = min(layer + 1, merged_image.shape[1] - 1)
    elif change == 'previous':
        layer = max(layer - 1, 0)
    choose_layer = merged_image[:, layer, :, :]
    plt.imshow(choose_layer[:, :, 0], cmap='gray')
    plt.draw()

# Funkcje do obsługi przycisków
def next_layer(event):
    update_layer('next')

def previous_layer(event):
    update_layer('previous')

plt.imshow(choose_layer[:,:,0],cmap='gray')
# Tworzenie przycisków
ax_next = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_prev = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_next = Button(ax_next, 'Next')
btn_next.on_clicked(next_layer)
btn_prev = Button(ax_prev, 'Previous')
btn_prev.on_clicked(previous_layer)


#wyswietlanie jednej warstwy (wybor x,y,z czyli prawo lewo, przod tyl, gora dol)

plt.show()
