import cv2


def load_face_detector():
    detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    return detector


def initialize_camera(camera_index=0):
    camera = cv2.VideoCapture(camera_index)
    return camera


def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray


def detect_faces(detector, gray_frame):
    faces = detector.detectMultiScale(
        gray_frame,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return faces


def draw_faces(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame


def display_face_count(frame, count):
    cv2.putText(
        frame,
        f"Faces Detected: {count}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )


def run_face_detection():
    face_detector = load_face_detector()

    # Check if cascade loaded correctly
    if face_detector.empty():
        print("Error: Could not load Haar Cascade file.")
        return

    camera = initialize_camera()

    # Check if camera opened
    if not camera.isOpened():
        print("Error: Could not access the camera.")
        return

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        gray = preprocess_frame(frame)

        faces = detect_faces(face_detector, gray)

        frame = draw_faces(frame, faces)

        display_face_count(frame, len(faces))

        cv2.imshow("Real-Time Face Detection", frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_face_detection()