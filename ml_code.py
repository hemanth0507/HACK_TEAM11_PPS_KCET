# -*- coding: utf-8 -*-
"""ml_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A3yHb2GDO09UkougZYq5fdV225k4dI7D
"""

!pip install tensorflow keras

# ✅ Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import os

# ✅ Load your trained model
model_path = "/content/D_fruit_model.h5"  # Adjust this path if needed
model = load_model(model_path)
print("✅ Model loaded")

# ✅ Load and preprocess test image
test_image_path = "/content/red-apple - Nimble Narmadha.jpg"  # Replace with your image path
img = image.load_img(test_image_path, target_size=(224, 224))
plt.imshow(img)
plt.axis('off')
plt.title("Test Image")
plt.show()

img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.  # Normalize

# ✅ Define class names (make sure these match your model training)
class_names = ['Apple', 'Banana', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Pear', 'Pineapple', 'Watermelon']

# ✅ Make prediction
prediction = model.predict(img_array)
predicted_index = np.argmax(prediction)
confidence = prediction[0][predicted_index]
predicted_class = class_names[predicted_index]

# ✅ Display prediction result
print(f"🍎 Predicted Class: {predicted_class}")
print(f"🔍 Confidence: {confidence:.2f}")

