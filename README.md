# 🖼️ Image Editing App with OpenCV

An interactive web-based image editor built with **Streamlit** and **OpenCV** that allows you to apply various filters and adjustments to your images in real-time.

## Features

This application provides a comprehensive set of image editing tools:

- **Blur Filter** - Adjustable blur effect (kernel size: 1-51)
- **Sharpness Control** - Enhance image sharpness (0.0-3.0)
- **Brightness Adjustment** - Brighten or darken images (-100 to +100)
- **Contrast Control** - Adjust image contrast (0.5-3.0)
- **Edge Detection** - Apply Canny edge detection with customizable thresholds
- **Grayscale Conversion** - Convert images to black and white
- **Real-time Preview** - Side-by-side comparison of original and edited images
- **Download Edited Images** - Save your edited images as PNG files

## Tech Stack

- **Streamlit** - Web application framework
- **OpenCV (cv2)** - Image processing library
- **Pillow (PIL)** - Image handling
- **NumPy** - Numerical computations
- **Python 3.x**

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Madhukar-Palakaveeti/image_editor.git
   cd image_editor
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit application, run:

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Usage

1. **Upload an Image** - Click on the "Upload Image" button and select a JPG or PNG file from your computer
2. **Apply Filters** - Use the sliders and checkboxes in the left sidebar to:
   - Adjust blur, sharpness, brightness, and contrast
   - Enable edge detection and adjust its thresholds
   - Convert to grayscale
3. **Preview Changes** - See the original and processed images side-by-side in real-time
4. **Reset** - Click the "Reset" button to restore all sliders to their default values
5. **Download** - Click the "Download Edited Image" button to save your edited image

## Project Structure

```
image_editor/
├── app.py              # Main Streamlit application
├── filters.py          # Image filtering functions
├── utils.py            # Utility functions for image handling
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Requirements

Key dependencies include:
- streamlit==1.57.0
- opencv-python==4.13.0.92
- pillow==12.2.0
- numpy==2.4.4
- pandas==3.0.3

For a complete list of dependencies, see `requirements.txt`

## Troubleshooting

**App won't start:**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're in the correct directory
- Try updating Streamlit: `pip install --upgrade streamlit`

**Image upload not working:**
- Ensure the image is in JPG or PNG format
- Check file size and permissions

## Future Enhancements

Potential features to add:
- Image rotation and flipping
- Crop functionality
- Color adjustments (saturation, hue)
- Filter presets
- Image export in multiple formats
- Batch image processing

