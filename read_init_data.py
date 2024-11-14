import pandas as pd
from typing import Union, Tuple
import numpy as np

def read_init_data(init_data_file:str, return_metrics:bool = False) -> Union[Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray, pd.DataFrame]]:
    # Read initial dataset
    init_data = pd.read_csv(init_data_file, header = None, index_col = False)

    # Set column names
    n_metric = 4
    n_dim = init_data.shape[1] - n_metric - 1 

    x_col = [f'x{i}' for i in range(n_dim)]
    metric_col = ['CPI','power','area','WTS']
    cols = x_col + metric_col + ['FOM']

    init_data.columns = cols 

    # Get input parameter sets, output FOM, and design metrics
    X = init_data[x_col].to_numpy()
    Y = init_data['FOM'].to_numpy()
    metrics = init_data[metric_col]

    if return_metrics:
        return X, Y, metrics
    else:
        return X, Y

if '__main__' == __name__:
    # Read parameter sets and FOM into numpy arrays
    X, Y = read_init_data('InitBoomDataset.csv')
    print('Shape of X is',X.shape,'\nShape of Y is',Y.shape)

    X, Y, metrics = read_init_data('InitRocketDataset.csv', True)
    print('Shape of X is',X.shape,'\nShape of Y is',Y.shape)
    print(metrics.shape)