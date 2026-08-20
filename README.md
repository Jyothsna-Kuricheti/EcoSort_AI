# ♻️ EcoSort_AI

## Smart Waste Classification Using Deep Learning & Custom CNN

EcoSort_AI is a deep learning-based computer vision project that automatically classifies waste images into different material categories.

The project uses a custom Convolutional Neural Network (CNN) to classify waste images into **12 different categories**. The main objective is to support automated waste segregation and contribute toward smarter and more sustainable waste management.

---

##  Problem Statement

Manual waste segregation is time-consuming, labor-intensive, and can lead to incorrect classification of recyclable and non-recyclable materials.

EcoSort_AI aims to address this challenge by using computer vision and deep learning to automatically identify waste materials from images.

---

##  Proposed Solution

EcoSort_AI takes a waste image as input and processes it using a custom CNN model.

The model learns important visual features such as:

- Edges
- Shapes
- Textures
- Patterns
- Material characteristics

After processing the image, the model predicts the most likely waste category using a Softmax classification layer.

---

##  Deep Learning Model

The project uses a custom Sequential CNN architecture consisting of:

- Conv2D
- MaxPooling2D
- Batch Normalization
- Flatten
- Dense
- Dropout
- Softmax

The final output layer contains **12 neurons**, representing the 12 waste categories.

---

##  Model Configuration

| Parameter | Configuration |
|---|---|
| Input Image Size | 160 × 160 × 3 |
| Batch Size | 32 |
| Maximum Epochs | 25 |
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Output Classes | 12 |
| Output Activation | Softmax |

---

##  Data Preprocessing

The input images are preprocessed before being provided to the CNN model.

The preprocessing pipeline includes:

- Image loading
- Image resizing
- Conversion to `float32`
- Pixel value normalization
- Batch generation

Pixel values are scaled to the range of **0 to 1** to make the training process more efficient.

---

##  Data Augmentation

Data augmentation is used to improve model generalization and reduce overfitting.

The project uses techniques such as:

- Rotation
- Width and height shifting
- Zooming
- Horizontal flipping

These transformations help the model learn from variations of the available training images.

---

##  Regularization & Training Optimization

Several techniques are used to improve training stability and reduce overfitting:

### Batch Normalization
Helps stabilize and speed up the training process.

### Dropout
Helps reduce overfitting by randomly disabling a portion of neurons during training.

### EarlyStopping
Stops training when the monitored validation performance no longer improves.

### ReduceLROnPlateau
Automatically reduces the learning rate when the validation performance reaches a plateau.

### Class Weight Balancing
Class weights are used to give more importance to underrepresented classes during training.

---

##  Model Evaluation

The trained model is evaluated using:

- Confusion Matrix
- Classification Report
- Precision
- Recall
- F1-score
- Class-wise performance

These metrics help understand how effectively the model distinguishes between different waste categories.

---

## 🛠️ Technology Stack

### Programming Language
- Python

### Deep Learning
- TensorFlow
- Keras
- Convolutional Neural Network (CNN)

### Computer Vision
- OpenCV

### Machine Learning & Evaluation
- Scikit-learn

### Data & Visualization
- NumPy
- Matplotlib

### Development Environment
- Jupyter Notebook

---

##  Project Structure

```text
EcoSort_AI/
│
├── app/
│   └── Application files
│
├── dataset/
│   └── Dataset information
│
├── models/
│   └── Trained model files
│
├── notebook/
│   └── Jupyter notebooks
│
├── presentation/
│   └── Project presentation
│
├── report/
│   └── Project report
│
├── requirements.txt
│
└── README.md
