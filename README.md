# Fashion MNIST Image Classification using CNN

An end-to-end deep learning project that classifies fashion product images into 10 categories using a Convolutional Neural Network (CNN). The project includes model training, image prediction through a web application, and Docker-based containerization.

## Project Overview

Fashion MNIST is a dataset of grayscale images representing clothing and fashion items. This project uses a CNN built with TensorFlow/Keras to learn image patterns and predict the category of a given fashion image.

The trained model is integrated into a web application so users can upload an image and obtain a predicted class. Docker is used to package the application and its dependencies into a container for consistent execution across environments.

## Objectives

- Build a CNN model for image classification.
- Preprocess and analyze the Fashion MNIST dataset.
- Train and evaluate a deep learning model.
- Develop an interactive image prediction application.
- Containerize the application using Docker.
- Organize the project for reproducibility and deployment.

## Technologies Used

- **Programming Language:** Python
- **Deep Learning:** TensorFlow / Keras
- **Data Processing:** NumPy
- **Web Application:** Streamlit
- **Containerization:** Docker
- **Development Tools:** Jupyter Notebook, VS Code / PyCharm
- **Version Control:** Git and GitHub

## Dataset

The project uses the Fashion MNIST dataset, which contains 70,000 grayscale images of size 28 × 28 pixels.

- Training images: 60,000
- Test images: 10,000
- Image dimensions: 28 × 28 pixels
- Number of classes: 10

### Fashion Categories

| Label | Category |
|---:|---|
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

Dataset source: [Fashion MNIST — GitHub](https://github.com/zalandoresearch/fashion-mnist)

## Project Workflow

1. **Data Preparation:** Load the dataset, inspect the images, normalize pixel values, and prepare labels.
2. **Model Development:** Build a CNN architecture using TensorFlow/Keras.
3. **Model Training:** Train the model on the training dataset.
4. **Model Evaluation:** Evaluate classification performance using the test dataset and appropriate metrics.
5. **Model Integration:** Load the trained model into the prediction application.
6. **Image Prediction:** Allow users to submit fashion images and view predicted categories.
7. **Dockerization:** Build a Docker image containing the application and its required dependencies.

## Project Structure

```text
Fashion-MNIST/
├── app/
│   ├── trained_model/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── model_training_notebook/
│   └── Fashion_MNIST_model_training.ipynb
├── test_images/
│   ├── fashion_mnist_1.png
│   ├── fashion_mnist_2.png
│   └── fashion_mnist_3.png
├── .gitignore
└── README.md
```

*Note: The structure above reflects the project layout; adjust filenames if your actual files differ.*

## Installation and Setup

### Prerequisites

- Python 3.10 or another version compatible with your installed dependencies
- Git
- Docker Desktop (for containerized execution)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/fashion-mnist-image-classification.git
cd fashion-mnist-image-classification
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Run with Docker

Ensure Docker Desktop is installed and running.

Build the Docker image:

```bash
docker build -t fashion-mnist-classifier ./app
```

Run the container:

```bash
docker run --rm -p 8501:8501 fashion-mnist-classifier
```

Open the application in your browser at:

http://localhost:8501

**Important:** The Dockerfile must expose port 8501 and start the Streamlit application on `0.0.0.0` for this command to work. If your application uses a different port or framework, adjust the commands accordingly.

### 3. Run Locally with Python

Create and activate a virtual environment.

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r app/requirements.txt
```

Start the application:

```powershell
python -m streamlit run app/main.py
```

If your project uses a different application entry point, replace `app/main.py` with the correct path.

## Model Evaluation

The trained CNN should be evaluated on the held-out test dataset. Useful evaluation metrics include:

- Test accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Add your actual test metrics and training plots here after verifying the results from your notebook. No performance figures are stated because the project's verified evaluation results have not been provided.

## Key Features

- CNN-based image classification
- Ten fashion category predictions
- Image preprocessing and model inference
- Interactive web application
- Docker-based application packaging
- Reproducible model training workflow

## Future Improvements

- Improve classification performance through model tuning and data augmentation.
- Add confidence scores and visual prediction explanations.
- Deploy the application to a cloud platform.
- Add automated testing and continuous integration.
- Compare CNN performance with other image classification architectures.

## Learning Outcomes

This project demonstrates practical experience with deep learning, image preprocessing, CNN model development, model inference, Python application development, Docker containerization, and Git-based version control.
