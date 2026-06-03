# Smart Photo Organizer

An AI-powered photo management system that automatically organizes large collections of images into meaningful categories using Deep Learning.

## Problem Statement

Most of us have thousands of photos scattered across pendrives, laptops, mobile devices, hard drives, and cloud storage. Manually organizing these images into folders is time-consuming and often neglected, making it difficult to locate specific photos later.

The goal of this project is to automate photo organization by classifying images into different categories and storing them in structured folders, reducing manual effort and improving accessibility.

## Project Overview

Smart Photo Organizer is a Deep Learning-based image classification system that automatically categorizes uploaded images into one of four categories:

* Selfies
* Passport-Size Photos
* Landscapes
* Objects

The model was trained on a custom dataset created and curated by me using images collected from multiple sources. The final Convolutional Neural Network (CNN) model achieved an accuracy of **83%** on the test dataset.

This project was developed as part of my B.Tech Minor Project in Artificial Intelligence and Data Science.

---

## Features

* Automatic image classification
* CNN-based Deep Learning architecture
* Categorization into four image classes
* Dataset created and curated manually
* 83% classification accuracy
* Google Colab-based training pipeline
* Jupyter Notebook implementation
* Easy integration with web applications and chatbots

---

## Dataset

The dataset used for training was manually created and curated for this project.

### Dataset Link

[Dataset Folder](https://drive.google.com/drive/folders/1pHPuNkDJIC12ji_GRdqPoPBMQtBzVEGf?usp=sharing)

The dataset contains images belonging to the following categories:

* Selfies
* Passport Photos
* Landscapes
* Objects

> Note: The dataset is hosted on Google Drive because of its large size.

---

## Trained Model

The trained Deep Learning model can be accessed using the following link:

[Download Trained Model](https://drive.google.com/file/d/1jdLZULHXdkE4Hy-5ymysJ84ykRhgSWgG/view?usp=sharing)

> The model is hosted separately due to GitHub file size limitations.

---

## Model Architecture

The project uses a Convolutional Neural Network (CNN) for image classification.

### Workflow

1. Collect and curate dataset
2. Perform image preprocessing
3. Resize and normalize images
4. Train CNN model on Google Colab using GPU acceleration
5. Evaluate model performance
6. Save trained model
7. Predict image category
8. Organize images into corresponding folders

---

## Technologies Used

### Programming Language

* Python

### Deep Learning

* TensorFlow
* Keras
* CNN

### Development Environment

* Google Colab
* Jupyter Notebook

### Libraries

* NumPy
* Pandas
* Matplotlib
* OpenCV
* TensorFlow/Keras

### Version Control

* Git
* GitHub

---

## Results

| Metric                  | Value            |
| ----------------------- | ---------------- |
| Classification Accuracy | 83%              |
| Categories              | 4                |
| Framework               | TensorFlow/Keras |
| Training Platform       | Google Colab     |

---

## Repository Structure

```text
minor-project/
│
├── Smart_Photo_Organizer.ipynb
├── Dataset_Link.txt
├── Model_Link.txt
├── README.md
└── Assets/
```

---

## Future Enhancements

* Duplicate image detection
* Face recognition integration
* Natural Language Query Support
* Chatbot-based image retrieval
* Streamlit Web Application
* Cloud Deployment
* Multi-label image classification

---

## Author

**R Puneet Kesava**

B.Tech - Artificial Intelligence and Data Science
BVRIT Narsapur

LinkedIn:
https://linkedin.com/in/puneet-kesava-a88163293

---

## Acknowledgement

This project was developed as part of my Minor Project under the guidance of **Prof. Santhosh Vishvakarma** and focuses on applying Deep Learning techniques to solve real-world photo management and organization problems.
