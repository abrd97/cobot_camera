import pyrealsense2 as rs
import numpy as np
import cv2
import os
from datetime import datetime

pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
pipeline.start(config)

snapshot_dir = './gt'
image_snapshot_count = 0



if not os.path.exists(snapshot_dir):
    print(f'Created: {snapshot_dir}')
    os.makedirs(snapshot_dir)


try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        
        if not color_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', color_image)

        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        key = cv2.waitKey(1) & 0xFF
        
        # Press 'q' to exit
        if key == ord('q'):
            break
        
        elif key == ord('s'):
            image_snapshot_count = image_snapshot_count + 1
            file_name = f'gt_{time_stamp}_{image_snapshot_count}'
            color_path = os.path.join(snapshot_dir, file_name + '.png')
            
            # create already ground truth label with same name
            with open( os.path.join(snapshot_dir, file_name + '.txt'), 'w') as file:
                pass
            
            cv2.imwrite(color_path, color_image)
            print(f"Saved snapshot ground truth and label to {snapshot_dir}")
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
