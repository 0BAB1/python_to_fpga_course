# Python AI to FPGA : Course Material

This repo contains all the course's material form my teaching activities (do not use outside the course, conform to french law intellectual property).

Lectures given at : [IDEC](https://www.idec.or.kr/) & [Sungkyunkwan University](https://www.skku.edu/eng/index.do).

> [!NOTE]  
> This course is 9 hours long and this repo is meant for teaching eveything people need to know to deploy end-to-end solutions.
> It was not meant to be done alone. Attending the lectures is indeed far more efficient but students can reach out to me if needed.

# Lectures

Examples are meant to be watched during the lectures to understand basic concepts, you can also follow along.

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
