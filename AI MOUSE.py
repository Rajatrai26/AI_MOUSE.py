import cv2                                      #package to access webcam to read video
import mediapipe as mp                          #package mediapipe named as mp
import pyautogui                                #package to move the cursor
cap = cv2.VideoCapture(0)         #use variable  cap to stor video captured by camera
hand_detector=mp.solutions.hands.Hands()                    #use mediapipe to store hand detection
drawing_utils=mp.solutions.drawing_utils                    #use drawing utils to draw
screen_width,screen_height=pyautogui.size()                 #to find screen height and width by calling pyautogui
index_y=0
while True:
    _, frame = cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands= output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)       #calling drawing utils to draw landmarks
            landmarks= hand.landmark
            for id,landmark in enumerate (landmarks):              #giving ids to fingers
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)

                if id==8:                                  #id 8 represent index finger
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))          #calling cv2 package to make circle on index finger
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_height*y
                    print('outside',abs(index_y-thumb_y))
                    if abs(index_y-thumb_y)<30:                       #condition for click when difference between index finger and thumb is less than 30
                        pyautogui.click()                              #calling pyautogui for click operation
                        pyautogui.sleep(1)

    cv2.imshow('virtual AI Mouse', frame)
    cv2.waitKey(1)


