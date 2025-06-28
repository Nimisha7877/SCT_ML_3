#SCT_ML_3

A machine learning project that implements a support vector machine to classify images of cats and dogs from kaggle Dataset. Customers are grouped based on their annual income and spending behavior to identify marketing-friendly clusters. | Internship @ SkillCraft Technologies

# 🐱🐶 Cat vs. Dog Image Classifier using SVM

This project is a simple machine learning solution to classify images as either a **Cat** or a **Dog** using a Support Vector Machine (SVM). It demonstrates basic image preprocessing, feature extraction, and model training for beginners working with computer vision tasks.

---

## 📌 Objective

🔎 Build a machine learning model to classify images as either **Cat** or **Dog** using a Support Vector Machine (SVM), aiming to:

- Understand basic image classification workflows
- Practice image preprocessing techniques
- Evaluate model performance on real-world image data

---

## 🗂️ Dataset Details

- **Dataset Name:** PetImages
- **Source:** [Microsoft PetImages Dataset](https://www.microsoft.com/en-us/download/details.aspx?id=54765)

### Folder Structure

| Folder / File Path                | Description               |
|-----------------------------------|---------------------------|
| PetImages/                        | Root folder for the dataset |
| PetImages/Cat/                    | Folder containing cat images |
| PetImages/Cat/cat_image1.jpg      | Example cat image file |
| PetImages/Cat/cat_image2.jpg      | Example cat image file |
| PetImages/Dog/                    | Folder containing dog images |
| PetImages/Dog/dog_image1.jpg      | Example dog image file |
| PetImages/Dog/dog_image2.jpg      | Example dog image file |

- Images vary in size and quality.
- Up to **500 images per class** are used for faster training.

---

## 🧠 Techniques Used

- Grayscale image conversion
- Image resizing to **64 × 64 pixels**
- Flattening images into 1D feature vectors
- Normalizing pixel values to range 0-1
- Support Vector Machine (SVM) with a linear kernel
- Train-test split (80% train, 20% test)
- Model evaluation using accuracy and classification report

---

## ✅ Output Example

### 📊 Model Evaluation Metrics:

Accuracy: 0.49

Classification Report:
               precision    recall  f1-score   support

         Cat       0.47      0.58      0.52        96
         Dog       0.51      0.40      0.45       104

    accuracy                           0.49       200
   macro avg       0.49      0.49      0.49       200
weighted avg       0.49      0.49      0.49       200

---

---

## 🚀 How to Run the Project

You can run this project locally using Python.

### 🔹 Option 1: Run Locally in VS Code

1. **Download and extract the PetImages dataset** into your local machine.

2. Open the project folder in **Visual Studio Code**.

3. Make sure your Python environment is selected in the bottom left (or use the Command Palette → “Python: Select Interpreter”).

4. Update the dataset path in your Python script:

```python
DATASET_PATH = r"C:\Users\tiwar\OneDrive\Desktop\Python\PetImages"
