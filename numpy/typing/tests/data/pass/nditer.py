import numpy as np

arr = np.array([1])
np.nditer([arr, None])
np.nditer([arr, arr, None], op_axes=[[0, -1], [-1, 0], None])
