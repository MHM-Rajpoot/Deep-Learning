import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

from deep_sort_realtime.deepsort_tracker import DeepSort

print("YOLOv8 model loaded successfully!")

model = YOLO('/content/v9/weights/best.pt')

tracker = DeepSort(
    max_iou_distance=0.7,
    max_age=30,
    n_init=3,
    nn_budget=100
)

video_path = "/content/videos/Test Vid 1.mp4"

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

output_video_path = "/content/tracked_output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

frame_count = 0
while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, verbose=False)

    detections = []

    pig_class_id = 0

    for r in results:
        boxes = r.boxes
        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())

            if cls == pig_class_id and conf > 0.75:

                bbox_xywh = [x1, y1, x2 - x1, y2 - y1]
                detections.append((bbox_xywh, conf, cls))

    tracked_objects = tracker.update_tracks(detections, frame=frame)

    for track in tracked_objects:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        ltrb = track.to_ltrb()

        x1, y1, x2, y2 = int(ltrb[0]), int(ltrb[1]), int(ltrb[2]), int(ltrb[3])

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 4)

        text = f"ID: {track_id}"
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 4)

    out.write(frame)

    frame_count += 1

    if frame_count % 100 == 0:
        print(f"Processed {frame_count} frames.")

cap.release()
out.release()

print(f"\nTracking complete! Output video saved to: {output_video_path}")