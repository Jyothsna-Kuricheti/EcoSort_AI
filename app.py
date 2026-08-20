# Import Libraries

import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="EcoSort AI",
    page_icon="♻️",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------

@st.cache_resource
def load_cnn_model():
    return load_model("../models/garbage_classifier_model.keras")

model = load_cnn_model()

# -----------------------------
# Class Labels
# -----------------------------

class_labels = [

    "battery",
    "biological",
    "brown-glass",
    "cardboard",
    "clothes",
    "green-glass",
    "metal",
    "paper",
    "plastic",
    "shoes",
    "trash",
    "white-glass"

]

# -----------------------------
# Waste Bin Mapping
# -----------------------------

bin_mapping = {

    "battery":"🟥 Hazardous Waste Bin",

    "biological":"🟩 Organic Waste Bin",

    "brown-glass":"🟨 Glass Recycling Bin",

    "cardboard":"🟦 Dry Waste Recycling Bin",

    "clothes":"🟪 Textile Recycling Bin",

    "green-glass":"🟨 Glass Recycling Bin",

    "metal":"⚪ Metal Recycling Bin",

    "paper":"🔵 Paper Recycling Bin",

    "plastic":"🟠 Plastic Recycling Bin",

    "shoes":"🟪 Textile Recycling Bin",

    "trash":"⚫ General Waste Bin",

    "white-glass":"🟨 Glass Recycling Bin"

}

# -----------------------------
# Title
# -----------------------------

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("♻️ EcoSort AI")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Project Information")

st.sidebar.write("""
This application uses a Convolutional Neural Network (CNN)
to classify waste into **12 categories** and recommends
the correct recycling bin.
""")

st.sidebar.markdown("---")

st.sidebar.subheader("📂 Categories")

for item in class_labels:
    st.sidebar.write("✅", item.title())

st.sidebar.markdown("---")

st.sidebar.success("Model Accuracy : 72.39%")

st.sidebar.info("Developed using TensorFlow + Streamlit")
st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#2E8B57;
    font-size:48px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:22px;
}

.description{
    text-align:center;
    font-size:18px;
    color:#555555;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<div class="main-title">
♻️ EcoSort AI
</div>

<div class="sub-title">
Smart Waste Classification using Deep Learning
</div>

<br>

<div class="description">
Upload an image of waste and let our AI classify it into the correct category and recommend the appropriate recycling bin.
</div>

<hr>
""",
unsafe_allow_html=True
)

# -----------------------------
# Image Upload
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload Waste Image",
    type=["jpg","jpeg","png"]
)

# -----------------------------
# Prediction
# -----------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image,
             caption="Uploaded Image",
             use_container_width=True)

    image = image.resize((160,160))

    image_array = np.array(image)

    image_array = image_array / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction)) * 100

    predicted_class = class_labels[predicted_index]
# =====================================
# Prediction Results
# =====================================

st.success("🎉 Prediction Successful!")

st.success(f"♻️ Predicted Category : {predicted_class.title()}")

st.info(f"⭐ Confidence : {confidence:.2f}%")

st.warning(f"🗑️ Recommended Bin : {bin_mapping[predicted_class]}")
# =====================================
# Celebration Effect
# =====================================

if confidence >= 80:
    st.balloons()

    st.success("🎉 Excellent! The model is highly confident about this prediction.")
    