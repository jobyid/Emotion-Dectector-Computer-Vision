import cv2

face_cascade  = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_cascade   = cv2.CascadeClassifier('haarcascade_eye.xml')

def dectect_face_smile(img):
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=4)
    smile_count = 0
    face_count = len(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)
        smile_count = len(smiles)
        for (sx,sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,255,0), 2)
        #eyes  = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=18)
        #for (ex,ey,ew,eh) in eyes:
          #  cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)
    if smile_count > 0:
        cv2.putText(img, "Happy", (x,y), cv2.FONT_HERSHEY_PLAIN,2, (0,0,255),)
    elif face_count > 0:
        cv2.putText(img, "Not Happy", (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), )
    return img


video = cv2.VideoCapture(0)
window = "Webcam"
cv2.namedWindow(window)

while True:
    ok, frame = video.read()
    if ok:
        img = dectect_face_smile(frame)
        cv2.imshow(window, img)

    if cv2.waitKey(1) == ord("q"):
        break
