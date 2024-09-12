# Python to FPGA Course 

This repo contains all the course's examples. It does not contain the slides, you can email me or ask the course supervisor.

Made in collaboration with [IDEC](https://www.idec.or.kr/).

# Lectures

Example Mmeant to be watched during the lectures to understand basic concepts, you can also follow along.

If these concepts are not acquired / understood, I strongly encourage you to look into deeper material. *(the notebooks contains clues on where to look for such material in the "Learn More" sections)*

# Labs

Meant to be done from scratch, I highly recommend you do them by yourself; by following along during the labs or at home.

Each Lab has its specificities so each folder contain a ```readme.md``` file to provide details & context to the student.

## Lab prerequisites :

- Linux system is prefered but not mandatory
- Python, Pytorch installed on your system
- Docker environement setup for FINN and Brevitas (see below)
- Xilinx tools Vivado, Vitis & Vitis HLS (2023 Version)
- A zynq board for inference

## Setup your docker environement for the lab in advance :

You can setup you docker environement by cloning [finn](https://github.com/Xilinx/finn) and running :

```bash
bash run_docker.sh notebook
```

This will setup notebook dev environement. Here is the [official tutorial](https://finn.readthedocs.io/en/latest/getting_started.html#running-finn-in-docker) to follow to also setup the environement vars.

```/tmp/finn_dev_username``` will be a common folder where you can examine compiled outputs.
