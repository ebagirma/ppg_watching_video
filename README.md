# Emotion Detection using PPG Data

## Abstract
This project leverages the DEAP dataset to recognize emotions through the analysis of physiological signals, with a particular focus on Photoplethysmography (PPG). Recognizing emotions in conversation can be pivotal for a variety of applications, such as healthcare, education, and human-computer interaction. Unlike traditional cues like facial expressions and speech, physiological signals offer a more reliable window into genuine emotional states as they are less susceptible to voluntary control.

## Introduction
Emotions are complex psycho-physiological experiences that manifest through various internal and external changes in the body. The ability to automatically recognize emotions has significant implications for enhancing human-machine interfaces. This repository contains code for an experimental setup designed to elicit spontaneous emotions during face-to-face conversations, capturing the resulting brain and physiological signals.

## Getting Started
To begin using this codebase for emotion detection with PPG data, follow the steps below:

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries: `pandas`, `matplotlib`, `seaborn`, `numpy`, `sklearn`, `tensorflow`, `keras`

## Presentation Video
**Conference:** IUI '22 - 27th Annual Conference on Intelligent User Interfaces

[![Watch the video](https://img.youtube.com/vi/AVR3gMXZwuU/0.jpg)](https://www.youtube.com/watch?v=AVR3gMXZwuU)



### Installation
1. Clone the repository to your local machine using `git clone`.
2. Install the necessary Python packages using `pip install -r requirements.txt` (ensure you have `pip` installed).


## Repository Structure
Below is the structure of the repository which includes scripts and files needed to replicate the studies and analyses mentioned in our published work:
   
```
├── cnn_lstm_classification.py # Script for CNN-LSTM classification
├── load_data.py               # Utility script for loading datasets
├── lstm_classification.py     # Script for LSTM classification
├── main.py                    # Main script for running the full pipeline
├── requirements.txt           # Required libraries for the project
├── simple_classification.py   # Script for simple classification methods
└── utils.py                   # Utilities for various tasks in the pipeline
```

## Usage
To run the emotion detection analysis:
1. Load your dataset following the DEAP dataset structure.
2. Run the `lstm_classification` function with the appropriate parameters.
3. Utilize the `visualize_physiological_data` function to visualize the features and emotion labels.

### Data Preparation
Before running the classification, ensure your data is preprocessed according to the DEAP dataset guidelines and structured appropriately for this codebase.

### Training the Model
Execute the script or use the provided functions in a Python environment to train the LSTM model on your PPG data.


## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Published Work
This project is based on research conducted by our team, and findings have been published in the following paper:

- Saffaryazdi, N., Goonesekera, Y., Saffaryazdi, N., Hailemariam, N. D., Temesgen, E. G., Nanayakkara, S., Broadbent, E., & Billinghurst, M. (2022). Emotion recognition in conversations using brain and physiological signals. In Proceedings of the 27th International Conference on Intelligent User Interfaces (pp. 229-242).

We recommend reading the paper to understand the depth of the research and the methodologies applied.

## Citation
If you use this code or the associated dataset for your research, please cite our paper:

```bibtex
@inproceedings{saffaryazdi2022emotion,
  title={Emotion recognition in conversations using brain and physiological signals},
  author={Saffaryazdi, Nastaran and Goonesekera, Yenushka and Saffaryazdi, Nafiseh and Hailemariam, Nebiyou Daniel and Temesgen, Ebasa Girma and Nanayakkara, Suranga and Broadbent, Elizabeth and Billinghurst, Mark},
  booktitle={27th International Conference on Intelligent User Interfaces},
  pages={229--242},
  year={2022}
}


