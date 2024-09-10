# LAB 3 Presentation

FINN Provides a very neat runtie environement based on Pynq.

However, you might want to run inference on other (unsuported) FPGA boards.

To do so, we will go over various techniques to make it work.

- 0 => Find the FINN exportoted stitched IP and integrate this to your vivado project
- 1 => Create our own "glue logic" IP to interface between the model and Xilinx's DMA IP
- 2 => Run synth & impl and export to vitis
- 3 => Create software to run inference using DMA's drivers

## What is in this folder ?

This folder contains :

- HARDWARE : The glue logic IP's System Verilog code (use ```git clone --recursive https://github.com/0BAB1/python_to_fpga_course.git``` flag to clone the sub repo if needed or access it [here](https://github.com/0BAB1/Axi-Stream-FIFO-for-FINN))
- SOFTWARE : The code we'll run in Vitis
- SOFTWARE : A data generator for C inference of MNIST data.

To add :

- A lab handout to summarize what's todo
- some screenshots of final vivado project
- Vivado project itself, if practical given all the IPs' subfolders