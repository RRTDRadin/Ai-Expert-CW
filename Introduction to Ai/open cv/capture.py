import cv2 
from datetime import datetime

cap= cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    display_frame = frame.copy()

    cv2.putText(display_frame, "Press S to Capture", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.putText(display_frame, "Press Q to Quit", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    
    cv2.imshow("Camera", display_frame)

    key= cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
