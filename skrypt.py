
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import os




# Wczytaj plik NIfTI
nifti_file = nib.load('a1.nii')

# Pobierz dane z pliku NIfTI
nifti_data = nifti_file.get_fdata()
multi_layer_data = np.zeros(nifti_data.shape)
nifti_data_view = nifti_data[:,:,:,1]

#voxels = np.random.randint(0, 2, size=(32, 32, 32))
# Tworzenie figury i osi 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.voxels(nifti_data_view, edgecolor='k')
plt.show()