import streamlit as st
from PIL import Image

import style


st.title("Imaginify")
st.write("Style Transfer made easy")

img=st.sidebar.selectbox(
    'select image',
    ('amber.jpg','pxfuel.jpg','colosseum.jpg','fish.jpg','lizard.jpg','fox.jpg','pyramind.jpg','Taj Mahel.jpg','Taj Mahel Palace.jpg','turtule.jpg','dp.jpg','jitesh.jpg','boy.jpg')
)

style_name=st.sidebar.selectbox(
    'select style',
    ('candy','mosaic','composition','Starry','Waves','rain_princess','udnie','la_mause')
)

model="saved_models/" + style_name + ".pth"

input_image="images/content-images/" + img
input_image=st.sidebar.file_uploader("Choose a file", type=['png', 'jpg'])

output_image="images/output-images/" + style_name + "-" + img
st.sidebar.header('Upload file')
st.write("### Source Image:")
image = Image.open(input_image)
st.image(image,width=400)

clicked =st.button("stylize")

if clicked:
    model= style.load_model(model)
    style.stylize(model, input_image,output_image)


    st.write("### Output Image:")
    image = Image.open(output_image)
    st.image(image, width=400)
