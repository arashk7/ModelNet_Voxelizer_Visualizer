import numpy as np
from vpython import *


class ak_visualizer:
    def __init__(self, voxel_size=50):
        self.voxel_size = voxel_size
        scene.forward = vector(-0.9, -0.9, -1)
    def visualize_voxel(self, voxel, color=vector(1, 1, 1)):

        for i in range(self.voxel_size):
            for j in range(self.voxel_size):
                for k in range(self.voxel_size):
                    if voxel[i, j, k, 0] >= 0.9:
                        boxy = box(pos=vector(j, i, k), size=vector(0.9, 0.9, 0.9),
                                   color=color,

                                   texture=textures.metal)
