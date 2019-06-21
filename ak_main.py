import numpy as np
from ModelNet_Voxelizer_and_Visualizer.ak_voxelizer import ak_voxelizer
from ModelNet_Voxelizer_and_Visualizer.ak_visualizer import ak_visualizer


source_path = 'D:\Dataset\ModelNet10\ModelNet10'
dest_path = 'D:\Dataset\ModelNet10\ModelNet10_vox'
object_list = {"bathtub", "bed", "chair", "desk", "dresser", "monitor", "night_stand", "sofa", "table", "toilet"}

print('Start process ... ')

voxelizer = ak_voxelizer(voxel_size=50)
voxelizer.convert_all(source_path, dest_path, object_list)

print('End process ...')

print('Visualize a model')

visualizer = ak_visualizer(voxel_size=50)
vox_dir = 'D:\Dataset\ModelNet10\ModelNet10_vox\sofa/train'
name = 'sofa_0058'
vox_path = vox_dir + '/' + name + '.npz'
voxel = np.load(vox_path)
voxel = voxel['arr_0']
voxel = np.reshape(voxel, (50, 50, 50, 1))
visualizer.visualize_voxel(voxel)

