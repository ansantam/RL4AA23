# ML School 2022 - Use Case DESY II

Reinforcement learning is a form of machine learning in which intelligent agents learn to solve complex problems by gaining experience. In current research, agents trained with reinforcement learning perform better than their human counterparts on problems that have historically been difficult for machines to solve. Particle accelerators are among the most advanced high-tech machines in the world. Modern scientific experiments place the highest demands on beam quality, making particle accelerator control extremely complex. In this session, we will learn how to optimise a particle accelerator with reinforcement learning using a practical example.


## Getting started

The hands-on part of this session requires that you install some dependencies. Please start by installing [*Anaconda*](https://www.anaconda.com/)  according to the instructions on their website.

Then download or clone this directory to your machine.

With Anaconda installed, run the following command in the cloned directory to create the reinforcement learning environment.

```bash
conda env create -f environment.yaml
```

Use the following command to activate the workshop environment.

```bash
conda activate use-case-desy-ii
```

Then start the Jupyter Lab by running

```bash
jupyter lab
```

You are now ready to run the notebooks! 🎉


## Troubleshooting

### git not found

It may be that you cannot clone the repository to your local machine because git is not installed. In that case, instead of using git, simply visit the [repository home page](https://github.com/desy-ml/mle-school-2022-use-case-desy-ii), click the green *Code* button and select *Download ZIP*.

### Encountered error while trying to install package. box2d-py

You might encounter this error on a Linux distribution that does not come with *gcc* installed by default (such as Ubuntu). Run the following commands to fix, then re-run the command to create the environment.

```bash
sudo apt install build-essential
conda env remove --name use-case-desy-ii
```
