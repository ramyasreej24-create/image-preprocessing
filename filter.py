"""
filter.py
All OpenCV image-processing operations live here.
Each function takes a NumPy image array (BGR) and returns a processed array.
"""

import cv2
import numpy as np


def apply_blur(image, ksize):
    """Gaussian blur. ksize must be odd and >=1."""
    ksize = max(1, int(ksize))
    if ksize % 2 == 0:
        ksize += 1          # fix: increment kernel size, don't modify pixels
    if ksize <= 1:
        return image
    return cv2.GaussianBlur(image, (ksize, ksize), 0)


def apply_sharpen(image, alpha):
    """Unsharp-mask sharpening. alpha = strength (0.0 - 3.0)."""
    if alpha <= 0:
        return image
    blurred = cv2.GaussianBlur(image, (0, 0), sigmaX=3)
    return cv2.addWeighted(image, 1 + alpha, blurred, -alpha, 0)


def apply_brightness(image, beta):
    """Linear brightness shift. beta = -100 to 100."""
    return cv2.convertScaleAbs(image, alpha=1.0, beta=beta)


def apply_contrast(image, alpha):
    """Contrast scaling around mid-point. alpha = 0.5 - 3.0."""
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)


def apply_edge_detect(image, thresh1, thresh2):
    """Canny edge detection, returned as a 3-channel BGR image."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    edges = cv2.Canny(gray, thresh1, thresh2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


def apply_grayscale(image):
    """Convert to single-channel grayscale."""
    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_all_filters(image, settings):
    """
    Apply the full filter pipeline in sequence, always starting from the
    ORIGINAL image (never a previously-filtered one), so filters don't
    compound on top of each other across reruns.
    """
    result = image.copy()

    result = apply_brightness(result, settings.get("brightness_beta", 0))
    result = apply_contrast(result, settings.get("contrast_alpha", 1.0))
    result = apply_blur(result, settings.get("blur_ksize", 1))
    result = apply_sharpen(result, settings.get("sharpen_alpha", 0.0))

    if settings.get("edge_detect_on", False):
        result = apply_edge_detect(
            result,
            settings.get("edge_thresh1", 100),
            settings.get("edge_thresh2", 200),
        )

    if settings.get("grayscale_on", False):
        result = apply_grayscale(result)

    return result
