from utils import read_image, preprocess_image, get_face_encodings, compare_faces

def compare_faces_from_files(file_stream1, file_stream2):
    # Read and preprocess the images
    image1 = preprocess_image(read_image(file_stream1))
    image2 = preprocess_image(read_image(file_stream2))

    # Get the face encodings for each image
    encodings1 = get_face_encodings(image1)
    encodings2 = get_face_encodings(image2)

    # Compare the faces and return the result
    return compare_faces(encodings1, encodings2)
