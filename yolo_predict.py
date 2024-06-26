from ultralytics import YOLO
import os
import cv2

model = YOLO(
            "trained/yerba_v3.pt"
        ) 

# Create VideoCapture object
INPUT_VIDEO = './video/21.Yerba_mate_taragui_500g.mp4'

# Read video
cap = cv2.VideoCapture(INPUT_VIDEO)
win_name = "Camera Preview"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# classes = 0
results = model(
    source=INPUT_VIDEO,
    stream=True,
    save=True,
    conf=0.6,
    imgsz=640,
    iou=0.9,  # classes=classes
)  # generator of Results objects

for r in results:
    boxes = r.boxes  # Boxes object for bbox outputs

    image = r.orig_img.copy()
    if boxes.cls.numel() > 0:
        classe = boxes.cls.tolist()
        label = r.names
        scores = boxes.conf.tolist()  # Confidence scores

        # Draw BBoxes on the image
        # for box, label, score in zip(boxes, labels, scores):
        for i, box in enumerate(boxes.xyxy):
            x1, y1, x2, y2 = map(int, box)  # box
            color = (0, 255, 0)  # Green color
            thickness = 2

            cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

            text = f"{label[int(classe[i])]} ({scores[i]:.2f})"
            print(text)

            cv2.putText(
                image,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                thickness,
            )

    cv2.imshow(win_name, image)

    # Wait for a key press and check the pressed key
    key = cv2.waitKey(1)  # & 0xFF
    if key == ord("q"):  # Press 'q' to exit
        break
    elif key == ord("n"):  # Press 'n' to show the next image
        continue

# Release VideoCapture and destroy windows
cap.release()
cv2.destroyAllWindows()

