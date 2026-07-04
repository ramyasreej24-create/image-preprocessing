"""
utils.py
Helper functions for converting between PIL, NumPy, and bytes formats.
Keeping these conversions here keeps app.py clean and focused on layout.
"""

import io
import numpy as np
import cv2
from PIL import Image


def pil_to_bgr(pil_image: Image.Image) -> np.ndarray:
    """
    Convert a PIL Image (RGB or RGBA) to an OpenCV-style BGR NumPy array.

    Args:
        pil_image: PIL Image object, as returned by Image.open().

    Returns:
        NumPy array in BGR channel order, ready for OpenCV functions.
    """
    # Make sure we have 3 channels (drop alpha if present)
    rgb_image = pil_image.convert("RGB")
    rgb_array = np.array(rgb_image)
    bgr_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2BGR)
    return bgr_array


def bgr_to_rgb(bgr_image: np.ndarray) -> np.ndarray:
    """
    Convert a BGR (OpenCV) NumPy array to RGB, for display with st.image()
    or for re-wrapping into a PIL Image.
    """
    if len(bgr_image.shape) == 2:
        # Already single-channel (grayscale) -- nothing to convert
        return bgr_image
    return cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)


def bgr_to_png_bytes(bgr_image: np.ndarray) -> bytes:
    """
    Convert a BGR (or grayscale) NumPy array into PNG-encoded bytes,
    suitable for st.download_button().

    Args:
        bgr_image: NumPy array, either grayscale (H, W) or BGR (H, W, 3).

    Returns:
        Raw PNG bytes.
    """
    if len(bgr_image.shape) == 2:
        # Grayscale image -- convert straight to PIL in "L" mode
        pil_image = Image.fromarray(bgr_image)
    else:
        rgb_image = bgr_to_rgb(bgr_image)
        pil_image = Image.fromarray(rgb_image)

    buffer = io.BytesIO()
    pil_image.save(buffer, format="PNG")
    return buffer.getvalue()


def load_uploaded_image(uploaded_file) -> np.ndarray:
    """
    Read a Streamlit UploadedFile object and return it as a BGR NumPy array.

    Args:
        uploaded_file: object returned by st.file_uploader().

    Returns:
        BGR NumPy array ready for OpenCV processing.
    """
    pil_image = Image.open(uploaded_file)
    return pil_to_bgr(pil_image)
