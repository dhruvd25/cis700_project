from __future__ import print_function
from PIL import Image
from os.path import join
import os
from scipy.io import loadmat
import torch.utils.data as data
from torchvision.datasets.utils import download_url, list_dir, list_files

class celebrity(data.Dataset):
    """IMDB-wiki Celeb Face Age Dataset"""
    """
    Args:
        mat_file (string): Path to the mat file with information about dataset.
        root_dir (string): Directory with all the images.
        transform (callable, optional): Optional transform to be applied
            on a sample.
    """

    def __init__(self, landmarks_frame, root_dir, transform = None):
        self.landmarks_frame = loadmat(landmarks_frame)
        self.root_dir = root_dir
        self.transform = transform

        self.image_folder = os.path.expanduser(root_dir)

    def __len__(self):
        return len(self.landmarks_frame['path'])


    def __getitem__(self, idx):
        img_name = self.landmarks_frame['path'][idx]
        image_path = join(self.image_folder,img_name).rstrip()
        image = Image.open(image_path).convert('RGB')
        label = self.landmarks_frame['labels'][0][idx]
        if self.transform:
            image = self.transform(image)
        return image,label
