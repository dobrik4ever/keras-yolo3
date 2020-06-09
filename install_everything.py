import requests
import os

def download(fname,url):
    r = requests.get(url)
    open(fname, 'wb').write(r.content)


print('Download CFG...')
url = 'https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg'
download('yolov3.cfg', url)

if 'yolov3.weights' not in os.listdir():
    print('Download weights...')
    url = 'https://pjreddie.com/media/files/yolov3.weights'
    download('yolov3.weights', url)
    print('Convert weights...')
    os.system('python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5')

if 'yolov3-tiny.weights' not in os.listdir():
    print('Download weights tiny...')
    url = 'https://pjreddie.com/media/files/yolov3-tiny.weights'
    # download('yolov3-tiny.weights', url)
    print('Convert weights tiny...')
    os.system('python convert.py yolov3-tiny.cfg yolov3-tiny.weights model_data/yolov3-tiny.h5')

def mult_command(cmds):
    tmp = ''
    for cmnd in cmds:
        tmp += cmnd + ' && '
    tmp = tmp[:-4]
    print(tmp)
    return tmp

cmds = ['conda create -n yolo python=3.5.2 -y',
        'conda install -c anaconda tensorflow-base=1.6.0 -y']

initial_cmds = [
        'conda activate yolo',
        'conda install requests -y',
        'conda install -c anaconda pillow -y',
        'conda install -c anaconda opencv -y',
        'conda install -c anaconda tensorflow-gpu=1.6.0 -y',
        'conda install -c anaconda keras-gpu=2.1.5 -y',
        'conda install matplotlib -y',
        'conda install -c anaconda tqdm -y']

# os.system(mult_command(cmds))
print('Done!')
