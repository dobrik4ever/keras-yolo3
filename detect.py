from yolo import YOLO
import cv2
from PIL import Image
import os
from tqdm import tqdm

class Detect:
    def __init__(self):
        pass
    
    def run(self):
        imgs_to_detect = os.listdir('imgs')
        pbar = tqdm(total=len(imgs_to_detect))

        ver = 'yolov3-tiny'
        if ver == 'yolov3-tiny':
            Y = YOLO(
                model_path='model_data/yolov3-tiny.h5',
                anchors_path='model_data/tiny_yolo_anchors.txt')
        elif ver == 'yolov3':
            Y = YOLO()
        else:
            raise ValueError('npnpnp')
            
        for i in imgs_to_detect:
            image = Image.open('imgs/{}'.format(i))
            r_image = Y.detect_image(image)
            r_image.save('detected/{}'.format(i))
            pbar.update(1)
        pbar.close()
        Y.close_session()
        print('DONE!')

if __name__ == '__main__':
    d = Detect()
    d.run()
    
