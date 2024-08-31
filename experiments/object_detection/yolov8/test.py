from ultralytics import YOLO
from ultralytics import settings

# Load a pretrained YOLO model (recommended for training)
model = YOLO("best_aug.pt")

print(settings)
# Perform object detection on an image using the model
results = model("/home/george/Documents/chownet_project/yolo_format/train/food/images/25.jpg",  save=True)


