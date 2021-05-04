import numpy as np
from load_data import load_deap_data
from physiological.preprocessing import physiological_preprocessing
import heartpy as hp
import matplotlib.pyplot as plt


PART_SECONDS = 1
LABEL_TYPE = "arousal"
PPG_SAMPLING_RATE = 128
IGNORE_TIME = 8

def plot_deap_data(x,y):
    # Loading deap dataset
    ppg_data, labels = \
        load_deap_data(label_type=LABEL_TYPE)

    all_processed_physiological = []
    for p in range(ppg_data.shape[0]):
        all_trials_physiological = []
        for t in range(ppg_data.shape[1]):
            # preprocessing
            # Ignores IGNORE_TIME seconds from the start of each trial
            data = ppg_data[p, t, 0, IGNORE_TIME*PPG_SAMPLING_RATE:]
            preprocessed_physiological = \
                physiological_preprocessing(data,
                                            sampling_rate=PPG_SAMPLING_RATE)

            all_trials_physiological.append(preprocessed_physiological)

        all_processed_physiological.append(all_trials_physiological)
    ppg_data = np.array(all_processed_physiological)
    print(ppg_data[x,y,:].shape)
    return ppg_data[x,y,:]


wd, m = hp.process(plot_deap_data(3,4), PPG_SAMPLING_RATE)
plot_object = hp.plotter(wd, m, show=True, title='some awesome title')
plt.close()
print(len(wd))
