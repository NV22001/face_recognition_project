import cv2
import dlib

# Load the pre-trained face detector
detector = dlib.get_frontal_face_detector()

# Load an image
image_path = "images/your_image.jpg"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = detector(gray)

# Draw rectangles around faces
for face in faces:
    x, y, w, h = (face.left(), face.top(), face.width(), face.height())
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
