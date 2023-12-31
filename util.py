import base64

import streamlit as st
from PIL import ImageOps, Image
import numpy as np
from keras.layers import Conv2D
import cv2


def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.
    Parameters:
        image_file (str): The path to the image file to be used as the background.
    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def classify(image, model, class_names):
    """
    This function takes an image, a model, and a list of class names and returns the predicted class and confidence
    score of the image.
    Parameters:
        image (PIL.Image.Image): An image to be classified.
        model (tensorflow.keras.Model): A trained machine learning model for image classification.
        class_names (list): A list of class names corresponding to the classes that the model can predict.
    Returns:
        A tuple of the predicted class name and the confidence score for that prediction.
    """
    #image = ImageOps.fit(image, (32, 32), Image.Resampling.LANCZOS)
    #image_array = np.asarray(image)
    #image = np.expand_dims(image_array,0)
    #image = image_array.reshape((1,32,32,3))
    
    #prediction = model(img)
    #index = np.argmax(prediction)
    #class_name = class_names[index]
    #confidence_score = prediction[0][index]
    
    #image = cv2.imread(image)
    image = cv2.resize(image, (32,32))
    image = np.expand_dims(image,0)
    class_name = class_names[int(np.argmax(model(image),1))]
    confidence_score = 1
    index = 0

    return class_name, confidence_score, index,