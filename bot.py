import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    #ресайз по х и у 
    frameresized = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.blur(hsv, (5, 5))  # наложение стрмной маски чбшной
    mask = cv2.inRange(hsv, (89, 124, 73), (255, 255, 255))
    #hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([38, 86, 0])


    upper_blue = np.array([121, 255, 255])
    #тута менять фильтр
   #mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #imgray = cv2.cvtColor(mask, 127, 255, 0)
    #ret, thresh = cv2.threshold(imgray, 127, 255, 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    counturs = sorted(contours, key=cv2.contourArea, reverse=True)
    for contour in counturs:

        cv2.drawContours(frame, counturs[0], -1, (255, 0, 255), 3)
        cv2.imshow("Counturs", frame)  # рисует рокно с конурами
        #cv2.imshow("Mask", mask)
       # cv2.imshow("ret",ret)
        #cv2.imshow("blur",blurred_frame)
    key = cv2.waitKey(1)
    if key == 27:
          break
cap.release()
cv2.destroyAllWindows()
