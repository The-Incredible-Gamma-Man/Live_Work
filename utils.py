import cv2
import numpy as np
from PIL import Image
import face_recognition
import io

def read_image(file_stream):
    # Convert the image file stream to a NumPy array
    file_bytes = np.asarray(bytearray(file_stream.read()), dtype=np.uint8)
    # Decode the NumPy array into an image
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    image = image[:, :, ::-1]
    return image

def preprocess_image(image):
    # Resize image for faster face recognition processing
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    return image

def get_face_encodings(image):
    # Given an image, return the 128-dimension face encoding for each face in the image.
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    return face_encodings

def compare_faces(encodings1, encodings2):
    # Compare two lists of face encodings and return True if there are matches
    # This assumes that each list of encodings is from the same person
    # Adjust the tolerance parameter as needed
    matches = face_recognition.compare_faces(encodings1, encodings2, tolerance=0.6)
    return any(matches)
