import os
import typing

import cv2  # pytype: disable=attribute-error
import matplotlib
import numpy as np
import torch
import tqdm


def get_mean_and_std(dataset: torch.utils.data.Dataset,
                     samples: int = 128,
                     batch_size: int = 8,
                     num_workers: int = 4):

    if samples is not None and len(dataset) > samples:
        indices = np.random.choice(len(dataset), samples, replace=False)
        dataset = torch.utils.data.Subset(dataset, indices)
    dataloader = torch.utils.data.DataLoader(
        dataset, batch_size=batch_size, num_workers=num_workers, shuffle=True)

    n = 0  # number of elements taken (should be equal to samples by end of for loop)
    s1 = 0.  # sum of elements along channels (ends up as np.array of dimension (channels,))
    s2 = 0.  # sum of squares of elements along channels (ends up as np.array of dimension (channels,))
    for (x, *_) in tqdm.tqdm(dataloader):
        x = x.transpose(0, 1).contiguous().view(3, -1)
        n += x.shape[1]
        s1 += torch.sum(x, dim=1).numpy()
        s2 += torch.sum(x ** 2, dim=1).numpy()
    mean = s1 / n 
    std = np.sqrt(s2 / n - mean ** 2)  

    mean = mean.astype(np.float32)
    std = std.astype(np.float32)

    return mean, std

