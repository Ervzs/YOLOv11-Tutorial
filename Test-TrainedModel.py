# Import necessary libraries
from ultralytics import YOLO
import cv2


# Load your trained YOLO model (replace 'best.pt' with the path to your best-trained model)
model = YOLO(r"C:\_YOLO-Tutorial\runs\detect\train2\weights\best.pt")


results = model(r"C:\_YOLO-Tutorial\Image-Test\6.jpg", conf=0.1, show=True)
cv2.waitKey(0)
print(model.names)
