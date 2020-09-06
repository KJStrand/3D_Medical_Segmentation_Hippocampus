"""
This file contains code that will kick off training and testing processes
"""
import os
import json
import numpy as np

from experiments.UNetExperiment import UNetExperiment
from data_prep.HippocampusDatasetLoader import LoadHippocampusData

class Config:
    """
    Holds configuration parameters
    """
    def __init__(self):
        self.name = "Basic_unet"
        self.root_dir = r"/home/workspace/src/TrainingSet/"
        self.n_epochs = 10
        self.learning_rate = 0.0002
        self.batch_size = 32 # 8
        self.patch_size = 64
        self.test_results_dir = "/home/workspace/src/results/"

if __name__ == "__main__":
    # Get configuration
    c = Config()

    # Load data
    print("Loading data...")

    data = LoadHippocampusData(c.root_dir, y_shape = c.patch_size, z_shape = c.patch_size)


    # Create test-train-val split
    # In a real world scenario you would probably do multiple splits for 
    # multi-fold training to improve model quality

    keys = range(len(data))
    
    # Here, random permutation of keys array is useful in case if we do something like 
    # a k-fold training and combining the results.
    keys = np.random.permutation(keys)

    split = dict()

    # Create three keys in the dictionary: "train", "val" and "test". In each key, store
    # the array with indices of training volumes to be used for training, validation 
    # and testing respectively.
    split['train'] = keys[0:int(0.7*len(keys))] # 70% training data
    split['val'] = keys[int(0.7*len(keys)):int(0.9*len(keys))] # 20% validation data
    split['test'] = keys[int(0.9*len(keys)):] # 10% testing data
    
    # Verify that the sets don't overlap:
    assert(not bool(set(split['train']) & set(split['val'])))
    assert(not bool(set(split['val']) & set(split['test'])))
    
    # Set up and run experiment
    
    exp = UNetExperiment(c, split, data)

    # You could free up memory by deleting the dataset
    # as it has been copied into loaders
    # del dataset 

    # run training
    exp.run()

    # prep and run testing

    results_json = exp.run_test()

    results_json["config"] = vars(c)

    with open(os.path.join(exp.out_dir, "results.json"), 'w') as out_file:
        json.dump(results_json, out_file, indent=2, separators=(',', ': '))

