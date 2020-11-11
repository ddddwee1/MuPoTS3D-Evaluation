import scipy.io as sio 
import numpy as np 
import pickle 

data = pickle.load(open('two_stage_results.pkl', 'rb'))
def get_pred(seq_idx, frame_idx):
    res = np.float32(data[seq_idx][frame_idx][3])
    return res.transpose([0,2,1])

if __name__=='__main__':
	print(get_pred(1, 1).shape)
