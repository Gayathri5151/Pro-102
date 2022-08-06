import cv2
import time
import random
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videocaptureobject= cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame= videocaptureobject.read()
        imagename = 'New picture 1' + '.png'
        cv2.imwrite(imagename, frame)
        start_time= time.time
        result = False
    return imagename
    print('snapshot taken')    
    videocaptureobject.release()
    cv2.destroyAllWindows()
def main():
    while True:
        if((time.time()-start_time)>=5):
            name= take_snapshot()
main()            
