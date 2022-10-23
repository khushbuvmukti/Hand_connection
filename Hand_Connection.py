import cv2
import time
import mediapipe as mp

cap=cv2.VideoCapture(0)
mphand=mp.solutions.hands
hands=mphand.Hands()
mpdraw=mp.solutions.drawing_utils
ptime=0
ctime=0

while True:
    ret,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hands.process(imgrgb)
    # print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,handlms,mphand.HAND_CONNECTIONS)
            for id,lm in enumerate(handlms.landmark):
                # print(id,lm)
                h,w,x= img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                # if id==4:
                cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)





    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)





    cv2.imshow("img",img)
    key=cv2.waitKey(1)
    if key==27:
        break