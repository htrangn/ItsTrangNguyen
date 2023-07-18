from types import GeneratorType
import streamlit as st
import cv2
import numpy as np
from PIL import Image

import base64

main_bg = "sample.jpg"
main_bg_ext = "jpg"

side_bg = "sample.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

filename = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(filename)

@st.cache
def load_image(img):
    im = Image.open(img)
    return im

def detect_faces(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Face detection
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    #Draw rectangle
    for (x, y, width, height) in faces:
        cv2.rectangle(img, (x, y), (x+width, y+height), (255, 0, 0), 2)
    return img, faces

def main():
    #Face detection App
    st.title("Face detection App")
    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    #Detection
    if choice == "Detection":
        st.subheader("Face Detection")

        #Use Webcam
        image_file = st.camera_input(label = "Take a pic of you")

        #Upload img
        if image_file is None: image_file = st.file_uploader("Upload Image", type = ['jpg', 'png', 'jpeg'])

        #Face detection
        if st.button("Process"):
            if image_file is not None:
                our_image = Image.open(image_file)
                result_img, result_faces = detect_faces(our_image)
                st.image(result_img)
                st.success("Found {} face(s)".format(len(result_faces)))

            else: st.write("You haven't upload any image file")
    #About
    elif choice == "About":
        st.subheader("About this app")
        st.write("This app was made by Lê Trần Nguyên Ngọc and Nguyễn Hà Trang")
        st.write("Special thanks to JCharisTech, 1littlecoder, NeuralNine and Adarsh Menon for your useful videos on Youtube")

main()
