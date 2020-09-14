import scipy.io as sio 
import numpy as np 

data_dict = {}
def get_pred(seq_idx, frame_idx):
    global data_dict
    if not seq_idx in data_dict:
        data = sio.loadmat('./results/%d.mat'%seq_idx)['preds']
        data_dict[seq_idx] = np.float32(data)
    data = data_dict[seq_idx]
    return data[frame_idx]
