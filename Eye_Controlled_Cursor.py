#-------------@By Subhamoy Paul----------------
import cv2
import mediapipe as md
import pyautogui as pg
camera=cv2.VideoCapture(0)
face_mesh=md.solutions.face_mesh.FaceMesh(refine_landmarks=True)
sw, sh=pg.size()
while True:
    _, frame=camera.read()
    frame=cv2.flip(frame,1)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=face_mesh.process(rgb)
    points=result.multi_face_landmarks
    fh,fw,_=frame.shape
    if points:
        pt=points[0].landmark
        for i,landmark in enumerate(pt[474:478]):
            x=int(landmark.x*fw)
            y=int(landmark.y*fh)
            cv2.circle(frame,(x,y),3,(0,255,0))
            if i==1:
                sx=sw/fw*x
                sy=sh/fh*y
                pg.moveTo(sx,sy)
        left=[pt[145],pt[159]]
        for landmark in left:
            x = int(landmark.x * fw)
            y = int(landmark.y * fh)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if(left[0].y-left[1].y)<0.004:
            pg.click()
            pg.sleep(1)
    cv2.imshow('ecm',frame)
    cv2.waitKey(1)