# RetinaNet Model Deployment on i.MX8+ Device

## Overview
This project, a capstone endeavor by graduate students from the Engineering Artificial Intelligence program at CMU, focuses on the quantization and deployment of the RetinaNet model on the i.MX8+ device. The project aims to enhance the capabilities of the i.MX8+ device in handling advanced AI models, with a particular focus on applications in global health scenarios.

## Client
Global Health (GH) Laboratories: Contact (Michael Deeds, Global Health Laboratories, michael.deeds@ghlabs.org
)

## Contributors
- Bereket Adego Retta, Carnegie Mellon University-Africa bretta@andrew.cmu.edu  
- Gabrial Ashungafac Zencha, Carnegie Mellon University-Africa, gzenchaa@andrew.cmu.edu
- Jeannette Uwizeyimana, Carnegie Mellon University-Africa, juwizeyi@andrew.cmu.edu 
- Natasha Mutangana, Carnegie Mellon University-Africa, nmutanga@andrew.cmu.edu 


*Note: All contributors are graduate students in the Engineering Artificial Intelligence program at Carnegie Mellon University.*

## Project Description
Global Health Labs, Inc. (GH Labs) is a nonprofit organization based in Bellevue, Washington, USA, that develops innovative technologies to address unmet healthcare needs, especially in low- and middle-income countries. There is a critical healthcare disparity in low- and middle-income countries (LMICs), particularly concerning cervical cancer screening. These communities often face limited access to advanced medical technology, which leads to late detection and intervention for pre-cancerous lesions.

GH Labs has been working with partners to develop and deploy a machine learning-based cervical cancer screening system for low- and middle-income countries such as Rwanda, Zambia, Malawi, Senegal, and India. This system currently runs on Samsung phones; however, these phones have a short shelf life of about 9 to 12 months and need to be changed or updated frequently. These changes require multiple model adaptations that increase their costs and render them unsuitable for long-term deployment in resource-constrained environments.

The purpose of this project is to further the development and optimization of the Automated Visual Examination (AVE) system for cervical cancer detection by transitioning the AVE system from its current Android-based implementation to a more widely deployable, standalone medical device with a longer shelf life of 5 to 10 years. This product will provide a cost-effective, long-lasting solution to cervical cancer screening and ensure easy accessibility and improved healthcare outcomes in low- and middle-income countries.


## Installation and Setup
The following setup are tested on Linux based operating systems. 
- Personal Computer for Development (OS: Ubuntu 20.04)
    - Pytorch Retinanet 
        - For eeveloping a Retinanet Model from scract using pytorch, please follow the instructions on https://github.com/yhenon/pytorch-retinanet
        - NB: Pytorch can only be quantized to ONNX Models. Notes on Quantization are in the Quantization directory on this repository
    - Pytorch Retinanet 
        - For developing a Retinanet Model from scract using Keras, please follow the instructions on https://github.com/fizyr/keras-retinanet
        - NB: Keras can be converted to TensorFlow Lite (TF-Lite) models which can be quantized directly or also converted to ONNX models
- I.MX 8 PLUS Device
    - A machine learning image should be booted to the device 
    - TensorFlow Lite for I.mx which instructions on how to build can be found here https://github.com/nxp-imx/tensorflow-imx
    - Ensure the libvx_delegate.so is available on the device by checking in the /usr/bin/ for installed libraries.
    - Python OpenCV is also required can be installed with *pip install opencv-python*

## Usage
Information on how to run inference on the deployed models can be found in the inference directory



## Acknowledgments
Special thanks to Global Health Laboratories for their support and collaboration in this project. Their dedication to improving global health outcomes has been a key inspiration for our work.


---

This README is subject to updates as the project progresses.
