import cv2
import uuid
import os
import time

IMAGES_PATH = os.path.join('final_25_signs', 'workspace', 'Images', 'Collectimg' )

# Create label folders
for label in labels:
    label_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(label_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            continue
        imgname = os.path.join(label_path, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
