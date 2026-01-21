# Real-Time Emotion Recognition System using OAK Cameras
*This project is developed as part of an Undergraduate Research program advised by Prof. Dr. Josue J. G. Ramos.*

## 📄 About the Project

This repository documents the development of an **Undergraduate Research** project focused on **Affective Computer Vision**. The main objective is to develop and integrate a system capable of detecting human emotions in real-time, utilizing Deep Learning models optimized for GPU execution and OAK smart cameras.

In addition to the main system, this repository also houses the **foundational studies** and **exploratory data analysis** required to build the final pipeline.

## 🎯 Objectives

The project is divided into three strategic phases:
1. **Model Selection and Optimization:** Identifying efficient architectures for emotion detection.
2. **Hardware Integration (OAK):** Deploying the model on OAK-D hardware using DepthAI.
3. **Experimental Validation:** Testing latency and accuracy in real-world scenarios.

## 📂 Repository Structure

The project file structure mirrors the learning path and development stages:

* **`kaggle/FER2013/`**: Contains preliminary studies on the dataset, including scripts for data visualization (`visualize_faces.py`) and statistical analysis (`statistics.py`).
* **`studies/`**: Dedicated to mastering the core technologies used in the project.
    * **`numpy_studies/`**: Fundamental array manipulation and mathematical operations.
    * **`Pytorch_studies/`**: Introduction to tensors and neural network construction using PyTorch.

## 🛠️ Methodology

The adopted methodology follows a flow of incremental complexity:

* **Preliminary Studies (Kaggle & Fundamentals):** Analysis of the FER2013 dataset and technical leveling in NumPy/PyTorch (currently in the `studies` folder).
* **Hardware Familiarization:** Initial tests with OAK-D sensors.
* **Pipeline Implementation:** Training and optimizing the model.
* **Integration:** deploying the inference engine to the edge device.

## 🚀 Technologies Used

* **Language:** Python
* **AI Frameworks:** PyTorch
* **Libraries:** NumPy, Pandas, OpenCV
* **Hardware:** OAK-D Camera, GPU (CUDA)

## 📈 Expected Results

By the end of the project, the goal is to deliver a functional emotion recognition system using a camera, documented and experimentally validated regarding its capability to operate in real-time.