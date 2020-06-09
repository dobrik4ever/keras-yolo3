from yolo import YOLO
import cv2
from PIL import Image
import os
from tqdm import tqdm


class Detect:
    def __init__(self,ver='yolov3'):
        self.ver = ver

    def run(self):
        # folder = 'augmentation/rotated'
        folder = 'augmentation/noise'
        imgs_to_detect = os.listdir(folder)

        if self.ver == 'yolov3-tiny':
            Y = YOLO(
                model_path='model_data/yolov3-tiny.h5',
                anchors_path='model_data/tiny_yolo_anchors.txt')
        elif self.ver == 'yolov3':
            Y = YOLO()
        else:
            raise ValueError('npnpnp')

        for i in imgs_to_detect:
            image = Image.open('{}/{}'.format(folder,i))
            r_image = Y.detect_image(image)
            r_image.save('{}/box_{}'.format(folder,i))
        Y.close_session()
        print('DONE!')


if __name__ == '__main__':
    d = Detect()
    d.run()
