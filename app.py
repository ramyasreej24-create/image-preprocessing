"""
app.py
Main Streamlit entry point for the Image Editing App.
Run with: streamlit run app.py
"""

import streamlit as st

import filter as filters          # fix: file is named filter.py, not filters.py
from utils import load_uploaded_image, bgr_to_rgb, bgr_to_png_bytes

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Image Editor", page_icon="🖼️", layout="wide")
st.title("🖼️ Image Editing App")
st.caption("Upload an image, tweak it with the controls in the sidebar, and download the result.")

# ---------------------------------------------------------------------------
# Default settings + session_state init (needed so Reset actually works)
# ---------------------------------------------------------------------------
DEFAULT_SETTINGS = {
    "blur_ksize": 1,
    "sharpen_alpha": 0.0,
    "brightness_beta": 0,
    "contrast_alpha": 1.0,
    "edge_detect_on": False,
    "edge_thresh1": 100,
    "edge_thresh2": 200,
    "grayscale_on": False,
}

for key, default_value in DEFAULT_SETTINGS.items():
    if key not in st.session_state:
        st.session_state[key] = default_value


def reset_filters():
    """Callback for the Reset button: restore every widget to its default."""
    for key, default_value in DEFAULT_SETTINGS.items():
        st.session_state[key] = default_value


# ---------------------------------------------------------------------------
# Sidebar controls (all widgets bound to session_state via `key=`)
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Filter Controls")

    st.button("🔄 Reset all filters", on_click=reset_filters, use_container_width=True)

    st.subheader("Blur")
    st.slider("Kernel size (odd values only)", 1, 51, step=2, key="blur_ksize")

    st.subheader("Sharpness")
    st.slider("Sharpen strength", 0.0, 3.0, step=0.1, key="sharpen_alpha")

    st.subheader("Brightness")
    st.slider("Brightness shift", -100, 100, step=1, key="brightness_beta")

    st.subheader("Contrast")
    st.slider("Contrast multiplier", 0.5, 3.0, step=0.1, key="contrast_alpha")

    st.subheader("Edge Detect")
    st.checkbox("Enable Canny edge detection", key="edge_detect_on")
    st.slider("Lower threshold", 0, 500, step=1, key="edge_thresh1",
              disabled=not st.session_state["edge_detect_on"])
    st.slider("Upper threshold", 0, 500, step=1, key="edge_thresh2",
              disabled=not st.session_state["edge_detect_on"])

    st.subheader("Grayscale")
    st.checkbox("Convert to grayscale", key="grayscale_on")

# ---------------------------------------------------------------------------
# File uploader
# ---------------------------------------------------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load once per upload; cache in session_state so re-running on every
    # slider tweak doesn't re-decode the file from scratch.
    if (
        "original_image" not in st.session_state
        or st.session_state.get("uploaded_file_name") != uploaded_file.name
    ):
        st.session_state["original_image"] = load_uploaded_image(uploaded_file)
        st.session_state["uploaded_file_name"] = uploaded_file.name

    original_bgr = st.session_state["original_image"]

    current_settings = {key: st.session_state[key] for key in DEFAULT_SETTINGS}
    processed_bgr = filters.apply_all_filters(original_bgr, current_settings)

    col_original, col_processed = st.columns(2)
    with col_original:
        st.subheader("Original")
        st.image(bgr_to_rgb(original_bgr), use_container_width=True)
    with col_processed:
        st.subheader("Processed")
        st.image(bgr_to_rgb(processed_bgr), use_container_width=True)

    png_bytes = bgr_to_png_bytes(processed_bgr)
    st.download_button(
        label="⬇️ Download processed image (PNG)",
        data=png_bytes,
        file_name="processed_image.png",
        mime="image/png",
        use_container_width=True,
    )
else:
    st.info("👆 Upload a JPG, JPEG, or PNG file to get started.")
