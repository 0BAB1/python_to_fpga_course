# LAB 2 : Using FINN to convert our model to HW.

FINN is an incredible tool that allows us to convert common AI tensor operations into HW Layers.

The tool is still under active research and development. The generated layers depend on the architecture you chose.

You have to think about your achitecture in way that enables FINN to do its work, it is the whole subject of this LAB.

After the course, you might want to check these docs in order to make your own large classifiers that involves deeper work on the model :
- [FINN Docs](https://finn.readthedocs.io/en/latest/)
- [FINN additional ressources & papers](https://xilinx.github.io/finn/quickstart)

But for now, you can stick to the lab and I'll try my best to explain as much tricky moves as possible.

## 1 - Processing the model

We will operate some light processing on the model, adding labels, ...

## 2 - Verify the model

Now that the model is in FINN-ONNX Format, verifying it using actual data that you might use for inference is important.

We will use a wrapper provided by FINN to execute the model directly from the ONNX representation and check if our accuracy is coherent.

## 3 - Convert to HW Layers

We will then perform a series of transformations on the model, the goal here is to give the network a certain shape that FINN we be able to work with.

This step is where quantization and architecture choice may be important.

## What's next ?

FINN provides a pretty neat workflow for beginners that uses PYNQ : Python drivers & runtime, automated HW conversion for standards model etc..

My goal in this course was to :
- Give deeper understanding of the ways things works
- Implement the final product on Zynq

As the Zynq board I'll will use is not suppported, like many others, we will hack our way around and create our own logic using the produced IP, Vivado and Vitis worflow with some custom RTL along the way !
