import numpy as np
import cv2
from PIL import Image
import io

# Read image(from file uploader or file path)
def read_image(file):
    ''' Reads image and returns opencv format (BGR)
    works with Streamlit uploader or file path'''
    pil_image=Image.open(file).convert("RGB")
    cv_image=cv2.cvtColor(np.array(pil_image),cv2.COLOR_RGB2BGR)
    return cv_image

# Convert PIL image to opencv BGR Image format
def pil_to_cv(image_pil):
    '''Convert PIL Image to opencv BGR image format'''
    image_np = np.array(image_pil)
    image=cv2.cvtColor(image_np,cv2.COLOR_RGB2BGR)
    
    return image

# Convert opencv image to PIL RGB image format
def cv2_to_pil(image_cv):
    '''Covert opencv image to PIL RGB image format '''
    image =Image.fromarray(cv2.cvtColor(image_cv,cv2.COLOR_BGR2RGB))
    return image

def image_to_bytes(image):
    buf=io.BytesIO()
    image.save(buf,format="PNG")
    return buf.getvalue()

