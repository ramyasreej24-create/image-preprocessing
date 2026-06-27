import streamlit as st
from PIL import Image
import numpy as np
import filters
import utils

st.set_page_config(page_title="Image Editor",page_icon="🖼️",layout="wide")
st.title("🖼️ Image Editing App with Opencv")

# sidebar controls
st.sidebar.header("Filters")
blur=st.sidebar.slider("Blur",1,51,1,step=2)
sharpness=st.sidebar.slider("Sharpness",0.0,3.0,1.0,step=0.1)
brightness=st.sidebar.slider("Brightness",-100,100,0)
contrast=st.sidebar.slider("Contrast",0.5,3.0,1.0,step=0.1)

edge_toggle=st.sidebar.checkbox("Edge Detection",value=False)
if edge_toggle:
     t1=st.sidebar.slider("Canny Thresh 1",0,255,100)
     t2=st.sidebar.slider("Canny Thresh 2",0,255,200)
else:t1=t2=100

gray_toggle=st.sidebar.checkbox("Greyscale",value=False)

# Reset Button
if st.sidebar.button("Reset"):
    st.rerun()

# File upload
uploaded_file=st.file_uploader("Upload Image",type=["jpg","jpeng","png"])

if uploaded_file:
    image=utils.read_image(uploaded_file)
    processed=image.copy()

    # apply filters in sequence
    processed=filters.apply_blur(processed,blur)
    processed=filters.apply_sharpness(processed,sharpness)
    processed=filters.apply_brightness(processed,brightness)
    processed=filters.adjust_contrast(processed,contrast)


    if edge_toggle:
           processed=filters.apply_edge_detection(processed,t1,t2)

    if gray_toggle:
           processed=filters.apply_convert_grayscale(processed)


    # convert PIL for display
    original_pil=utils.cv2_to_pil(image)
    processed_pil=utils.cv2_to_pil(processed)
    col1,col2=st.columns(2)

    with col1:
        st.subheader("Original")
        st.image(original_pil,width='stretch')

    with col2:
        st.subheader("processed")
        st.image(processed_pil,width='stretch')  

    # Download
    img_bytes=utils.image_to_bytes(processed_pil)

    st.download_button(label="Download Edited Image",
                   data=img_bytes,
                   file_name="edited_image.png",
                   mime="image/png")


else:
     st.info("Upload an image to start aditing.")

