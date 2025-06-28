import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

DATASET_PATH = r"C:\Users\tiwar\OneDrive\Desktop\Python\PetImages"
IMG_SIZE = 64
MAX_SAMPLES_PER_CLASS = 500

X = []
y = []

class_map = {
    'Cat': 0,
    'Dog': 1
}

for class_name in ['Cat', 'Dog']:
    folder = os.path.join(DATASET_PATH, class_name)
    count = 0
    for filename in os.listdir(folder):
        if count >= MAX_SAMPLES_PER_CLASS:
            break
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        X.append(img.flatten())
        y.append(class_map[class_name])
        count += 1

X = np.array(X) / 255.0  # normalize
y = np.array(y)

if len(X) == 0:
    print("No images loaded. Please check folder paths and contents.")
    exit()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=["Cat", "Dog"]))
