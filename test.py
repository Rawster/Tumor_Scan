import voxelmap
import nibabel as nib
import numpy as np
from model import Voxels

def swap_values(array):
    return np.where(array > 0, 1, array)

nifti_file = nib.load('a1.nii')
nifti_data = nifti_file.get_fdata()
nifti_data_view = nifti_data[:,:,:,1]
nifti_data_view = swap_values(nifti_data_view)
model = voxelmap.Model(nifti_data_view)

VoxelsArray = np.array(Voxels)
model = voxelmap.Model(VoxelsArray)


# map each voxel embedding (int) to a particular [color, alpha_transparency] combination
model.hashblocks ={1: ['#bfff00',1], 2:['#c18bff',1], 3:['#37aa97',1],4:['magenta',1],5:['cyan',1]}

model.draw(geometry="voxels")