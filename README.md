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

NOTE : The training dataset and trained CNN model are not included in this repository because of file-size and distribution considerations.
The dataset and trained model are maintained separately for project development and deployment.

## Model Results

The trained CNN model was evaluated on **3,100 test images** using accuracy, precision, recall, F1-score, and a classification report.

### Overall Performance

| Metric | Score |
|---|---:|
| Accuracy | **73%** |
| Macro Average Precision | **0.67** |
| Macro Average Recall | **0.68** |
| Macro Average F1-score | **0.67** |
| Weighted Average Precision | **0.75** |
| Weighted Average Recall | **0.73** |
| Weighted Average F1-score | **0.73** |

### Class-wise Performance

| Waste Category | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Battery | 0.66 | 0.60 | 0.63 |
| Biological | 0.70 | 0.84 | 0.76 |
| Brown Glass | 0.79 | 0.76 | 0.78 |
| Cardboard | 0.70 | 0.79 | 0.75 |
| Clothes | 0.92 | 0.85 | **0.88** |
| Green Glass | 0.76 | 0.74 | 0.75 |
| Metal | 0.34 | 0.58 | 0.43 |
| Paper | 0.72 | 0.77 | 0.74 |
| Plastic | 0.57 | 0.64 | 0.60 |
| Shoes | 0.69 | 0.62 | 0.65 |
| Trash | 0.72 | 0.55 | 0.62 |
| White Glass | 0.51 | 0.45 | 0.48 |

### Observations

- The model achieved an overall accuracy of **73%**.
- The highest F1-score was achieved for the **Clothes** category at **0.88**.
- The model also performed well on **Brown Glass, Biological, Cardboard, and Green Glass**.
- **Metal** and **White Glass** were more challenging categories for the model.
- The difference in class-wise performance indicates that some waste categories may require additional training data or further model optimization.
