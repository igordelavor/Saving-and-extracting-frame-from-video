import cv2
  
#vidcap = cv2.VideoCapture("/home/igor/Documentos/monoVO-python-master/video_teste.mp4")
#success,image = vidcap.read()
#count = 0
#"/home/igor/Documentos/monoVO-python-master/other-database/0.jpg"
#gray = cv2.imread("/home/igor/Documentos/monoVO-python-master/other-database/0.jpg", 0)
  
#cv2.imshow('Gray image', gray)
  
#cv2.waitKey(0)
#cv2.destroyAllWindows()
import numpy as np
import cv2

# Capture video from file
cap = cv2.VideoCapture('video_teste.mp4')
count = 0

while True:

    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imwrite('%d.png' % count, gray)

        print('Read a new frame: ', ret)

        count += 1

        #cv2.imshow('frame',gray)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
#while success:    
  #ret, frame = capture.read()
#  grayFrame = image.convert('L')
#  success, grayFrame = vidcap.read()
  #success,image = vidcap.read()
  #grayFrame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#  cv2.imwrite("%d.png" % count, grayFrame)
 
  #cv2.imshow('video gray', grayFrame)
  #cv2.imshow('video original', frame)
  #print('Read a new frame: ', success)
  #count += 1
      
    #if cv2.waitKey(1) == 27:
    #    break
#capture.release()
#cv2.destroyAllWindows()
#for image in range(286):
  #new_img = image.convert('LA').convert('RGB')