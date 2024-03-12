from torch.utils.data.dataset import Dataset
from torch import tensor
import pandas as pd
import numpy as np


class EPSdataset(Dataset):
    def __init__(self, csv_file, transfrom=None):
        super().__init__()
        self.annotation = pd.read_csv(csv_file)
        self.transform = transfrom

    def __len__(self):
        return len(self.annotation)

    def __getitem__(self, index):
        sample = np.array(self.annotation.iloc[index])
        X = sample[:-1]
        y = sample[-1:]
        return tensor(X), tensor(y)
    
