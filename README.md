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

- Github repository containing the material: [https://github.com/ansantam/RL4AA23](https://github.com/ansantam/RL4AA23)
- Tutorial in slide form: [here](https://ansantam.github.io/RL4AA23/tutorial.slides.html#/)

## Getting started

- First, download the material to your local disk by cloning the repository:
`git clone https://github.com/ansantam/RL4AA23`
- If you don't have git installed, you can click on the green button that says "Code", and choose to download it as a `.zip` file.

### Setup the environment locally

- Open terminal app
- (Suggested) Create a virtual envrionment using `conda` or `venv`. 

#### venv

You need to have `venv` installed 
- For Mac: `sudo pip3 install virtualenv`
- For Linux: `sudo apt-get install python3-venv`

```
python3 -m venv rl4aa
source rl4aa/bin/activate
pip3 install -r requirements.txt
jupyter notebook
```

- Open the tutorial notebook `tutorial.ipynb` in the jupyter server in browser
- When you are done type `deactivate`

#### conda

Instructions to install conda [here](https://docs.conda.io/projects/conda/en/4.6.1/user-guide/install/index.html)

```
conda -n rl4aa python=3.10
conda activate rl4aa
cd path_to_your_folder/RL4AA23
pip3 install -r requirements.txt
jupyter notebook
```

- Open the tutorial notebook `tutorial.ipynb` in the jupyter server in browser
- When you are done type `source deactivate`
