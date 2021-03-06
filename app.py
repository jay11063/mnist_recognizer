import cv2
from keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np


@st.cache(allow_output_mutation=True)
def load():
    return load_model('predict_model_ver3.h5')


model = load()

st.write('# Handwriting Number Recognizer')

CANVAS_SIZE = 192

col1, col2 = st.columns(2)

with col1:
    canvas = st_canvas(
        fill_color='#000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas'
    )

if canvas.image_data is not None:
    img = canvas.image_data.astype(np.uint8)
    img = cv2.resize(img, dsize=(28, 28))
    # preview_img = cv2.resize(img, dsize=(
    #     CANVAS_SIZE, CANVAS_SIZE), interpolation=cv2.INTER_NEAREST)

    # col2.image(preview_img)

    x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = np.resize(x, (1, 784))
    result = model.predict(x).squeeze()
    # result = np.where(result[0] == 1)

    st.write('## Result: %d' % np.argmax(result))
