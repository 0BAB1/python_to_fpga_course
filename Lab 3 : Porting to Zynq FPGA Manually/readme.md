FINN Provides a very neat runtie environement based on Zynq.

However, you might want to run inference on other, unsuported board (Zynq based).

To do so, we will go over various techniques to make it work.

- 0 => Find the FINN exportoted stitched IP and integrate this to your vivado project
- 1 => Create our own "glue logic" IP to interface between the model and Xilinx's DMA IP
- 2 => Run synth & impl and export to vitis
- 3 => Create software to run inference using DMA's drivers