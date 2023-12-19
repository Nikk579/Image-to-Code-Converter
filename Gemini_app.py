import streamlit as st
import google.generativeai as genai
from PIL import Image
from IPython.display import display

# Custom CSS for the Streamlit app
custom_css = f"""
.main {{
  background-image: linear-gradient( 68.4deg,  rgba(99,251,215,1) -0.4%, rgba(5,222,250,1) 100.2% );
}}
.column-widget {{
    margin: 1em;
}}
"""

st.markdown(
    f"""
    <style>
        {custom_css}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Image to Code Converter")
def input_image(img):
    
    image = Image.open(img)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the uploaded file to PIL.Image.Image
    img_pil = Image.open(img)
    
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(["Given an uploaded screenshot depicting a user interface or any design element, generate the HTML and CSS code necessary to recreate the visual representation of the screenshot. The code should aim to faithfully capture the structure and styling of the original design. Consider the arrangement of elements, colors, fonts, and any other visual attributes. Provide the output as a well-organized and readable HTML and CSS code snippet. also add the gradient background to this file body and use colors as in the image : ", img_pil], stream=False)
    response.resolve()

    with col2:
        st.text_area("Generated Code", value=response.text, height=300,  key="output_text_area")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image(uploaded_file)
