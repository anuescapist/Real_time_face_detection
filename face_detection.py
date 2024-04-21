import cv2
face_cap = cv2.CascadeClassifier('C:/Users/anush/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
video_cap = cv2.VideoCapture(0)
while True :
    ret, video_data = video_cap.read()
    if not ret:
        print("Error capturing video")
        break
    gray = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces =face_cap.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(50,30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x,y,w,h) in faces:
         cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0), 2)
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("b"):
        break
video_cap.release()