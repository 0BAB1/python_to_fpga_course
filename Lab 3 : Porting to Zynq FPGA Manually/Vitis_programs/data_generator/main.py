# This generates an header file with N MNIST flatten sample
# data is 8bits INT8 (or just char) meant to be imported
# into a Tx buffer for use in Vitis (for DMA).
# we can then use labels to compare execution

import torch
from torchvision import datasets, transforms

# Load MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

mnist_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

# Select 20 random samples
num_samples = 20 # Add more samples if you want to measure accuracy
# For this lab, we'll stock to a simple demonstration so N = 20 for readability.
indices = [i for i in range(num_samples)]
print(indices)
samples = [mnist_dataset[i][0] for i in indices]
labels = [mnist_dataset[i][1] for i in indices]
print(labels)

# Generate C header file
with open('mnist_samples.h', 'w') as f:
    f.write("// This file has been auto-generated\n\n")
    f.write("#ifndef MNIST_SAMPLES_H\n")
    f.write("#define MNIST_SAMPLES_H\n\n")
    f.write("#define NUM_SAMPLES 20\n")
    f.write("#define IMAGE_SIZE 784\n\n")
    
    f.write("const unsigned char mnist_samples[NUM_SAMPLES][IMAGE_SIZE] = {\n")
    
    for i, sample in enumerate(samples):
        # Denormalize, scale to 0-255, and flatten
        img = (sample.squeeze()).clamp(0, 1) * 255
        img_flat = img.reshape(-1).byte().tolist()
        
        f.write("    {")
        f.write(", ".join(map(str, img_flat)))
        f.write("},\n")
    
    f.write("};\n\n")

    f.write("const unsigned char mnist_labels[NUM_SAMPLES] = {\n")

    for j, label in enumerate(labels):
        f.write("    " + str(label) + ",\n")
    
    f.write("};\n\n")
    f.write("#endif // MNIST_SAMPLES_H\n")

print("MNIST samples have been generated and saved in 'mnist_samples.h'")