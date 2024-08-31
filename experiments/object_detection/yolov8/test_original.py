from ultralytics import YOLO
from ultralytics import settings
import cv2

# Load the image
image_path = '/home/george/Documents/chownet_project/yolo_format/valid/food/images/95.png'
label_path = '/home/george/Documents/chownet_project/yolo_format/valid/food/labels/95.txt'
classes_path = '/home/george/Documents/chownet_project/yolo_format/classes.txt'
image = cv2.imread(image_path)
classes =  open('/home/george/Documents/chownet_project/yolo_format/classes.txt').read().split("\n")
print(classes)

bounding_boxes = [
[classes[72], 0.5657747067799144, 0.594532986541167, 0.6277651965655459, 0.8109340269176648],
[classes[32], 0.7256739676104357, 0.32004557075467466, 0.4785184023086769, 0.38952161475488706],
[classes[99], 0.10225794754008283, 0.568773031087293, 0.20451589508016565, 0.5230459750591304],
[classes[98], 0.34151748343318117, 0.4812072740921114, 0.27874202610772186, 0.7756264388919408]
]

# Image dimensions
height, width, _ = image.shape

# Loop through bounding boxes and plot them on the image
for bbox in bounding_boxes:
    class_id, x_center, y_center, w, h = bbox
   
    # Convert YOLO normalized coordinates to pixel values
    x_center_pixel = int(x_center * width)
    y_center_pixel = int(y_center * height)
    w_pixel = int(w * width)
    h_pixel = int(h * height)
   
    # Calculate top-left and bottom-right corners
    x1 = int(x_center_pixel - w_pixel / 2)
    y1 = int(y_center_pixel - h_pixel / 2)
    x2 = int(x_center_pixel + w_pixel / 2)
    y2 = int(y_center_pixel + h_pixel / 2)
   
    # Draw the bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Optionally, add label with class ID
    label = f"Class {class_id}"
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Save the result image
output_path = '/home/george/Documents/chownet_project/yolo_format/1_with_bboxes.jpg'
cv2.imwrite(output_path, image)

output_path