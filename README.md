# 1st collaboration workshop on Reinforcement Learning for Autonomous Accelerators (RL4AA'23)

This repository contains the material for the second day of the [RL4AA'23](https://indico.scc.kit.edu/event/3280/overview) event.

# Workshop organizing committee

- Andrea Santamaria Garcia (KIT)
- Simon Hirländer (University of Salzburg)
- Jan Kaiser (DESY)
- Chenran Xu (KIT)

## Slides

- Welcome and basics of RL, Andrea Santamaria Garcia
- Advanced concepts in RL, Simon Hirländer
- RL in particle accelerator control: are we there yet?, Simon Hirländer

## Python tutorial: reinforcement learning implementation example

Github repository containing the material: [https://github.com/ansantam/RL4AA23](https://github.com/ansantam/RL4AA23)

## Getting started

- First, download the material to your local disk by cloning the repository:
`git clone https://github.com/ansantam/RL4AA23`
- If you don't have git installed, you can click on the green button that says "Code", and choose to download it as a `.zip` file.

### Setup the environment locally

- Open terminal app
- (Suggested) Create a virtual envrionment using `conda` or `venv`. Here we show the example using `conda`: `conda -n rl4aa python=3.10`
- Activate the virtual environment `conda activate rl4aa`
- Make sure your are in the correct directory `cd path_to_your_folder/RL4AA23`
- Install the dependencies `pip install -r requirements.txt`
- Start the jupyter notebook `jupyter notebook`
- Open the tutorial notebook `tutorial.ipynb` in the jupyter server in browser
