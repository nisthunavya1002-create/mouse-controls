import cv2
import mediapipe as mp
import pyautogui 
import numpy as np

screen_w, screen_h=pyautogui.size()

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1)
mp_draw=mp.solutions.drawing_utils


cap=cv2.VideoCapture(0)

prev_x,prev_y=0,0
smoothening=7


while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    h,w,_=img.shape
    rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lm_list=[]

            for id,lm in enumerate(handLms.landmark):
                cx,cy=int(lm.x*w),int(lm.y*h)
                lm_list.append((id,cx,cy))
            mp_draw.draw_landmarks(img,handLms, mp_hands.HAND_CONNECTIONS)
            if lm_list:
                x1,y1=lm_list[8][1],lm_list[8][2]
                x2,y2=lm_list[4][1],lm_list[4][2]
                x3,y3=lm_list[12][1],lm_list[12][2]
                screen_x=np.interp(x1,[0,w],[0,screen_w])
                screen_y=np.interp(y1,[0,h],[0,screen_h])
                curr_x=prev_x+(screen_x-prev_x)/smoothening
                curr_y=prev_y+(screen_y-prev_y)/smoothening

                pyautogui.moveTo(curr_x,curr_y)
                prev_x,prev_y=curr_x,curr_y

                def distance(p1,p2):
                    return np.hypot(p1[0]-p2[0],p1[1]-p2[1])
                if distance((x1,y1),(x2,y2))<30:
                    pyautogui.click()
                    cv2.putText(img,"Left Click",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                if distance ((x3,y3),(x2,y2))<30:
                    pyautogui.click()
                    cv2.putText(img,"Right Click",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Hand Gesture Controls",img)
    if cv2.waitKey(1) & 0xFF==27:
        break

   
cap.release()
cv2.destroyAllWindows()