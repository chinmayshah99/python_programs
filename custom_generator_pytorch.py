'''
    An example program for using custom generator in pytorch

    # MIT License
    # Copyright (c) 2019 Chinmay Shah
'''

import torch
from torch.utils.data import Dataset


class CustomDatasetGenerator(Dataset):
    def __init__(self, x_set_1, x_set_2, y_set):
        self.x1, self.x2, self.y = x_set_1, x_set_2, y_set

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return ([self.x1[idx], self.x2[idx]], self.y[idx])

x_1, x_2 = torch.rand((1, 20)), torch.rand((1, 20))
y = torch.randint(2, (1, 20))

dataset = CustomDatasetGenerator(x_1, x_2, y)

trainloader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=True, num_workers=2)
