import numpy as np
import cv2
import PIL
#----------------------------------------------------------------------
lips = cv2.imread('./lips.jpg', 0)
eyeeye = cv2.imread('./eye.jpg', 0)
face_detector = cv2.CascadeClassifier("./data/haarcascades/haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier("./data/haarcascades/haarcascade_eye.xml")
lips_detector = cv2.CascadeClassifier("./data/haarcascades/haarcascade_smile.xml")
eyeeyez = [eyeeye, eyeeye, eyeeye, eyeeye, eyeeye, eyeeye]
lipz = [lips, lips, lips, lips, lips, lips, lips]
ww, hh = (16, 16)

# smileyy= Image.open("./smiley.png").convert('RGBA')

# _, mask = cv2.threshold(im[:, :, 3], 0, 255, cv2.THRESH_BINARY)
smiley = cv2.imread('./smiley.png', -1)
# _, mask = cv2.threshold(smiley[:, :, :3], 0, 255, cv2.THRESH_BINARY)
# bgr = smiley[:, :, :3]
# gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
# alpha = smiley[:,:,3] # Channel 3
# alpha = alpha/255
# gray = gray/255
# smiley= gray*alpha
# cv2.imwrite('./inja.jpg', smiley)
#------------------------------------------------------------------

mode = (input('Enter number[1-4]:'))
video_cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:                            
    ret, frame = video_cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_detector.detectMultiScale(frame_gray, 1.7, 5, minSize=(100,100))
    eyes = eye_detector.detectMultiScale(frame_gray, 1.7, 5, minSize=(10,10))
    smiles = lips_detector.detectMultiScale(frame_gray, 1.3, 20, minSize=(15, 15))  
    if ret == False:
        break
    elif mode == '1':
        
        for i, face in enumerate(faces):
            x, y, w, h = face
            #cv2.rectangle(frame_gray, (x, y), (x+w,y+h), (0, 255, 0), 6)
            smiley_resized = cv2.resize(smiley, (w,h))
            bgr = smiley_resized[:, :, :3]
            gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
            alpha = smiley_resized[:,:,3] # Channel 3
            alpha = alpha/255
            gray = gray/255
            frame_gray[y:y+h, x:x+w] = ((gray*alpha)+(1-frame_gray[y:y+h, x:x+w])*(1-alpha))*255
    elif mode == '2':

        for k, smile in enumerate(smiles):
            z, t, c, v = smile
            cv2.rectangle(frame_gray, (z, t), (z+c,t+v), (0, 0, 255), 4)      
            lips_resized = cv2.resize(lipz[k], (c, v))
            frame_gray[t:t+v, z:z+c] = lips_resized

        for j, eye in enumerate(eyes):
            b, n, m, l = eye
            cv2.rectangle(frame_gray, (b, n), (b+m,n+l), (255,0 , 0), 2)
            eye_resized = cv2.resize(eyeeyez[j], (m, l))
            frame_gray[n:n+l, b:b+m] = eye_resized
    elif mode == '3':

        for i, face in enumerate(faces):
            x, y, w, h = face
            # cv2.rectangle(frame_gray, (x, y), (x+w,y+h), (0, 255, 0), 6)
            temp = cv2.resize(frame_gray[y:y+h,x:x+w], (ww, hh), interpolation=cv2.INTER_LINEAR)
            frame_gray[y:y+h,x:x+w]= cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
    elif mode == '4':
        for i, face in enumerate(faces):
            x, y, w, h = face
            # cv2.rectangle(frame_gray,(x,y),(x+w,y+h), (0, 255, 0), 2)       
            temp = frame_gray[y:y+h, x:x+w]            # height,width=img.shape
            # for o in range(w):
                # for p in range(h):
                #     temp[o, p] = temp[p, o]
            temp = temp[w-1: :-1, :]
            frame_gray[y:y+h, x:x+w] = temp


    cv2.waitKey(40) 
    cv2.imshow('output', frame_gray)




        
    
    
 

