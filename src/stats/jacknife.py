############################################################
# Jacknife Error Analysis for Monte Carlo Time Series Data #
# Abhishek Samlodia : July 03, 2024                        # 
############################################################
import numpy as np

def block_mean(block_index, block_size, data_array):
    """
    args:
        block_index (int) -> which block number to use for the data
        block_size (int) -> size of bin/block for Jacknife analysis
        data_array (1-dimensional numpy array of floats) -> entire data array
    returns:
        mean (float) -> average of the data for the specified block
    """
    # find the indices of the data-points corresponding to the specified block_index
    leftout_indices = [(block_size * (block_index - 1) + k) for k in range(block_size)]

    # compute the arithmetic mean for the data-points in data_array excluding the specified block
    effective_data = []
    for i in range(data_array.shape[0]):
        if i not in leftout_indices:
            effective_data.append(data_array[i]) 

    return np.average(np.array(effective_data))

def data_mean(blocks, block_size, data_array):
    """
    args:
        blocks (int) -> total number of bins/blocks to use for Jacknife analysis
        block_size (int) -> size of bin/block for Jacknife analysis
        data_array (1-dimensional numpy array of floats) -> entire data array
    returns:
        mean (float) -> average of the entire dataset
    """
    # create list of blocked-means for each block
    blocked_means = [block_mean(i, block_size, data_array) for i in range(1, blocks+1)]

    # compute and return the average of the blocked-means data
    return np.average(np.array(blocked_means))

def data_variance(blocks, block_size, data_array):
    """
    args:
        blocks (int) -> number of bins to use for Jacknife analysis
        block_size (int) -> size of bin/block for Jacknife analysis
        data_array (1-dimensional numpy array of floats) -> entire data array
    returns:
        standard deviation (float) -> standard deviation of the correlated dataset
    """
    # find the mean of the entire dataset
    mean = data_mean(blocks, block_size, data_array)

    # create list of variances for each block
    blocked_variance = [(block_mean(i, block_size, data_array) - mean)**2 for i in range(1, blocks+1)]

    # find the variance for the entire data
    variance = sum(blocked_variance)
    variance *= (1.0 - (1.0/float(blocks)))

    # return the standard deviation now
    return np.sqrt(variance)

def get_stats(blocks, start, data_array):
    """
    args:
        blocks (int) -> number of bins to use for Jacknife analysis
        start (int) -> number of initial datapoints to skip
        data_array (1-dimensional numpy array of floats) -> entire data array
    returns:
        mean (float) -> average of the entire dataset
        standard deviation (float) -> standard deviation of the correlated data
    """
    # find the block_size
    block_size = int(((data_array.shape[0])/blocks))

    # find the mean and standard deviation 
    avg = data_mean(blocks, block_size, data_array[start-1:])
    err = data_variance(blocks, block_size, data_array[start-1:])

    # return the mean and stdev
    return block_size, avg, err