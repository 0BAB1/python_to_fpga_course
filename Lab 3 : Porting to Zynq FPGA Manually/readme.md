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

# LAB 3 MANUAL

## 0 : Find the FINN exportoted stitched IP and integrate this to your vivado project

During LAB 2, we used FINN to generate a "stitched IP" that conviniently generated a zynq project for us. Regardless of the workflow you chose (FINN has multple workflows like a [CLI](https://finn.readthedocs.io/en/latest/command_line.html) or [Custom builders](https://finn.readthedocs.io/en/latest/command_line.html) that does all we did in LAB in a automated way), you will always have a collection of outputs including :

- The different layers as IPs
- A stitched IP

After LAB 2, you can access the stitched IP by opinning the ```/tmp/finn_dev_yourusername``` folder, you will then find a range of output product.
We are going to focus on the ```vivado_zynq_xxx.../``` folder and open the .xpr using vivado.

## 1 : Create our own "glue logic" IP to interface between the model and Xilinx's DMA IP

With the output vivado project oppened, we will now proceed to delete every IP used in the block design **except for the stiched IP**, we will keep it a build our system around it.

As we can see, the stiched IP is very conviently packed with simplifed stream interfaces and expects a 8bits input for the data, just as planed !

But there is a problem : to transfer data, we will use Xilinx's DMA IP that need TLAST signal to function properly.

You can create a custom FIFO IP using the HDL in this repo's folder in order to handle the correct signals assertion for DMA to function properly.
... to be continued (saving..)
