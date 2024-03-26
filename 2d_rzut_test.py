import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import Slider

# Ładowanie pliku nii
nifti_file = nib.load('a1.nii')
nifti_data = nifti_file.get_fdata()

# Skalowanie do koloru
data_scaled = nifti_data / np.max(nifti_data)
merged_image = np.stack((data_scaled[:, :, :, 0], data_scaled[:, :, :, 1], data_scaled[:, :, :, 2]), axis=-1)

# Wybór warstwy
layer = 60
choose_layer = merged_image[:, layer, :, :]
#wybor oritentacji (jeszcze nie zaimplementowane)
orientation = "top-bottom"
min_axis = 0
if  orientation == "top-bottom":
    max_axis = merged_image.shape[0] 
if  orientation == "front-bottom":  #sprawdzic czy to na pewno front-bottom
    max_axis = merged_image.shape[0] 
if  orientation == "side-side":    #sprawdzić czy to na pewno side-side
    max_axis = merged_image.shape[0] 


# Funkcja do aktualizacji warstwy
'''
def update_layer(change):
    global layer, choose_layer
    if change == 'next':
        layer = min(layer + 1, merged_image.shape[1] - 1)
    elif change == 'previous':
        layer = max(layer - 1, 0)
    choose_layer = merged_image[:, layer, :, :]
    plt.sca(ax_main)  # Ustawienie aktualnych osi na te, które wykorzystujemy do wyświetlenia obrazu
    plt.imshow(choose_layer[:, :, 0], cmap='gray')
    plt.draw()

'''
def update_layer(change):
    global layer, choose_layer
    plt.sca(ax_main) 
    choose_layer = merged_image[:, change, :, :]
    plt.imshow(choose_layer[:, :, 0], cmap='gray')
    plt.draw()


# Funkcje do obsługi przycisków
def next_layer(event):
    update_layer('next')

def previous_layer(event):
    update_layer('previous')

def change_layer(event):
    update_layer(slider.val)

# Wyświetlanie jednej warstwy
plt.figure()
ax_main = plt.axes()
plt.imshow(choose_layer[:, :, 0], cmap='gray')
'''
# Tworzenie przycisków
ax_next = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_prev = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_next = Button(ax_next, 'Next')
btn_next.on_clicked(next_layer)
btn_prev = Button(ax_prev, 'Previous')
btn_prev.on_clicked(previous_layer)
'''
#slider test
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')  # [left, bottom, width, height]
slider = Slider(ax_slider, 'warstwa', min_axis, max_axis, valinit=1.0, valstep=1)  # (axis, label, min, max, initial value)
slider.on_changed(change_layer)

plt.show()