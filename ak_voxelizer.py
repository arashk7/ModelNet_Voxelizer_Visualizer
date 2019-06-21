import numpy as np
import os


class ak_voxelizer:
    def __init__(self, voxel_size=50):
        self.voxel_size = voxel_size

    def convert_all(self, source_path, dest_path, object_list):
        for c in object_list:
            s_path = source_path + '/' + c
            d_path = dest_path + '/' + c
            os.chdir(dest_path)

            if not os.path.exists(d_path):
                os.mkdir(c)
            os.chdir(d_path)
            train_d_path = d_path + '/' + 'train'
            train_s_path = s_path + '/' + 'train'
            if not os.path.exists(train_d_path):
                os.mkdir('train')
            self.convert_dir(train_s_path, train_d_path)
            test_d_path = d_path + '/' + 'test'
            test_s_path = s_path + '/' + 'test'
            if not os.path.exists(test_d_path):
                os.mkdir('test')
            self.convert_dir(test_s_path, test_d_path)

    def convert_dir(self, source_dir, dest_dir):
        files = os.listdir(source_dir)
        print(dest_dir)
        for i in range(len(files)):
            off_path = source_dir + '/' + files[i]
            if os.path.isfile(off_path):
                if off_path.split('.')[1] == 'off':
                    # file_name = os.path.basename(off_path)
                    name = os.path.splitext(files[i])[0]
                    obj_path = dest_dir + '/' + name + '.obj'
                    self.convert_off_to_obj(off_path, obj_path)
                    npy_path = dest_dir + '/' + name + '.npy'
                    str = 'obj2voxel --size 50 ' + obj_path + ' ' + npy_path
                    os.system('obj2voxel --size 50 ' + obj_path + ' ' + npy_path)
                    os.remove(obj_path)
                    v = np.load(npy_path)
                    npz_path = dest_dir + '/' + name + '.npz'
                    np.savez_compressed(npz_path, v)
                    os.remove(npy_path)

    def convert_off_to_obj(self, off_path, obj_path):
        off_file = open(off_path, 'r')
        obj_file = open(obj_path, 'w')
        lines = off_file.read().split("\n")
        s = lines[1].replace("\n", "")
        s = s.split(" ")
        num_points = int(s[0])
        num_tri = int(s[1])

        for i in range(2, num_points + 2, 1):
            s = lines[i].split(" ")
            obj_file.write('v ' + s[0] + ' ' + s[1] + ' ' + s[2] + '\n')

        for i in range(num_points + 2, num_points + num_tri + 2, 1):
            s = lines[i].split(" ")
            obj_file.write('f ' + str(int(s[1]) + 1) + ' ' + str(int(s[2]) + 1) + ' ' + str(int(s[3]) + 1) + '\n')

        obj_file.close()


# source_path = 'D:\Dataset\ModelNet10\ModelNet10'
# dest_path = 'D:\Dataset\ModelNet10\ModelNet10_vox'
# object_list = {"bathtub", "bed", "chair", "desk", "dresser", "monitor", "night_stand", "sofa", "table", "toilet"}
#
# convert_all(source_path, dest_path, object_list)
#
# print('finish')
