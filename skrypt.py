import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

# Wczytaj plik NIfTI
nifti_file = nib.load('a1.nii')

# Pobierz dane z pliku NIfTI
nifti_data = nifti_file.get_fdata()[:, :, :, 1]  # Wybierz drugi wymiar 3D

# Określenie progu intensywności (np. 90 percentyla)
threshold = np.percentile(nifti_data, 90)

# Stworzenie maski na podstawie progu intensywności
mask = nifti_data >= threshold

# Tworzenie figury i osi 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Wyświetlenie tylko tych voxelów, które przekraczają próg
ax.voxels(mask, edgecolor='k')

plt.show()
