"""Eye Aspect Ratio utilities for the DriverSafe demo."""
import math

# MediaPipe Face Mesh landmark indices for the eye contours.
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def _distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def eye_aspect_ratio(points):
    """Calculate EAR from six (x, y) eye contour points."""
    if len(points) != 6:
        raise ValueError("EAR requires exactly six eye landmark points.")
    vertical_1 = _distance(points[1], points[5])
    vertical_2 = _distance(points[2], points[4])
    horizontal = _distance(points[0], points[3])
    if horizontal == 0:
        return 0.0
    return (vertical_1 + vertical_2) / (2.0 * horizontal)

def average_eye_ear(landmarks, width, height):
    """Return average EAR for both eyes from MediaPipe normalized landmarks."""
    def pixel_points(indices):
        return [(int(landmarks[i].x * width), int(landmarks[i].y * height)) for i in indices]
    left = eye_aspect_ratio(pixel_points(LEFT_EYE))
    right = eye_aspect_ratio(pixel_points(RIGHT_EYE))
    return (left + right) / 2.0
