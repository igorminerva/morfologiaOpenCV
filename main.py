import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.title("🔬 Morphology with OpenCV")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert to grayscale
    image = np.array(Image.open(uploaded_file).convert("L"))
    st.image(image, caption="Original Image", width='stretch')

    # Parameters
    operation = st.selectbox(
        "Choose operation",
        ["Erosion", "Dilation", "Opening", "Closing", "Gradient", "Top-hat", "Black-hat"]
    )
    kernel_size = st.slider("Kernel size", 1, 15, 5, step=2)
    iterations = st.slider("Iterations", 1, 5, 1)

    # Define kernel
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Apply morphology
    if operation == "Erosion":
        result = cv2.erode(image, kernel, iterations=iterations)
    elif operation == "Dilation":
        result = cv2.dilate(image, kernel, iterations=iterations)
    elif operation == "Opening":
        result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=iterations)
    elif operation == "Closing":
        result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=iterations)
    elif operation == "Gradient":
        result = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel, iterations=iterations)
    elif operation == "Top-hat":
        result = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel, iterations=iterations)
    elif operation == "Black-hat":
        result = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel, iterations=iterations)

    # Show processed image
    st.image(result, caption=f"Result: {operation}", width='stretch')

    # Download button
    result_pil = Image.fromarray(result)
    buf = io.BytesIO()
    result_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="💾 Download Result",
        data=byte_im,
        file_name="result.png",
        mime="image/png"
    )
